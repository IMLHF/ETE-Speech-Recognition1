import os

path_to_download = 'datasets'
base_model_path = 'model_saved'

os.makedirs(path_to_download, exist_ok=True)
os.makedirs(base_model_path, exist_ok=True)

test_model = base_model_path + ''
cache_dir = 'cache_unigram'

resume = {
	'restart': False,
	'model_path':
		''
}

use_cuda = True

if not use_cuda:
	num_cuda = '4'
	os.environ["CUDA_VISIBLE_DEVICES"] = num_cuda
else:
	num_cuda = '0'
