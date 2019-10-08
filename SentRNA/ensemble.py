import subprocess

for i in range(20):
    subprocess.check_output('python', 'run.py', '--mode' 'train', '--input_data', '../data/train/eterna_complete_ss.pkl', '--results_path', 'model%i' % i, '--n_long_range_features', '20')
    # Test test
    subprocess.check_output('python', 'run.py', '--mode', 'test', '--input_data', '../data/test/eterna100.pkl', '--test_model', 'test/model%i' % i, '--results_path', 'model_tested%i.pkl' % i)
    # Refine test
    subprocess.check_output('python', 'run.py', '--mode', 'refine', '--input_data', 'test_results/model_tested%i.pkl' % i, '--results_path', 'model_refined%i.pkl' % i)