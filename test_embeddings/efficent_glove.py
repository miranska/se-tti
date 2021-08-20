import argparse
import glob
import os
import re
from itertools import combinations
import pandas as pd
from gensim.models import KeyedVectors


def all_combinations(my_words):
    perm_list = []
    for i in range(1, len(my_words), 1):
        perm_list += list(combinations(my_words, i))

    return perm_list


def run_the_code(lines, model_dir, output_dir, top_n):
    # find the *.wv files in all subdirectories
    word_vectors_files = glob.glob(f"{model_dir}/**/*.wv", recursive=True)
    if len(word_vectors_files) == 0:
        print(f"There are no *.mv files in the '{model_dir}' or its subdirectories." +
              " Either point to a different directory or train the models first.")
        exit(1)

    stats_agg = []  # cumulative stats
    file_name = 'unknown'
    for wv_file_name in word_vectors_files:
        stats = []  # per-model stats
        wv = KeyedVectors.load_word2vec_format(wv_file_name, binary=False)

        file_name = re.search(r'^(.*?)\..*', os.path.basename(wv_file_name)).group(1)
        epoch = re.search(r'(?<=\.)\d+', os.path.basename(wv_file_name)).group()

        for line in lines:
            line = line.lower()
            my_words = line.split(" ")

            if len(my_words) == 1:  # If it is just one-word keyword it skips this case (e.g., "input")
                continue

            perm_list = all_combinations(my_words)
            all_expected_outputs = set(my_words)

            for perm in perm_list:
                perm_set = set(perm)
                expected_closest_words = all_expected_outputs.symmetric_difference(perm_set)
                try:
                    actual_closest_words = wv.most_similar(positive=perm_set, topn=top_n)
                    actual_closest_words = dict(actual_closest_words).keys()  # strip distances of the closest words
                    correct_words = expected_closest_words.intersection(actual_closest_words)

                    stats.append(
                        {
                            'test_case': line,
                            'file': file_name,
                            'epoch': epoch,
                            'input': str(perm_set),
                            'expected_output': str(expected_closest_words),
                            'correct_words': str(correct_words),
                            'expected_output_len': len(expected_closest_words),
                            'correct_words_len': len(correct_words),
                        }
                    )

                except KeyError as e:
                    if 'not in vocabulary' in str(e):
                        stats.append(
                            {
                                'test_case': line,
                                'file': file_name,
                                'epoch': epoch,
                                'input': str(perm_set),
                                'missing_word': str(e)
                            }
                        )
                    else:
                        raise

        stats_agg += stats
        pd.DataFrame(stats).to_csv(f'{output_dir}/{file_name}.{epoch}.csv')
    pd.DataFrame(stats_agg).to_csv(f"{output_dir}/_cumulative_stats.csv", index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run test cases against a set of models')
    parser.add_argument('-i', '--input', help='name of the root directory containing wv files', required=True)
    parser.add_argument('-o', '--output', help='name of the directory where the files should be stored',
                        default=f'{os.getcwd()}/ieee_glove_models_d')
    parser.add_argument('-t', '--test_case_file', help='name of the file with test cases',
                        default='test_cases.txt')
    parser.add_argument('-n', '--top_n', help='maximum number of closest words to select',
                        default=20)

    args = parser.parse_args()

    with open(args.test_case_file, 'r', encoding='utf-8', errors='ignore') as f:
        test_cases = [line.strip().encode('ascii', 'ignore').decode('utf-8') for line in f]

    if not os.path.exists(args.output):
        os.makedirs(args.output)
    print(f"Save output to {args.output}")

    run_the_code(test_cases, args.input, args.output, args.top_n)
