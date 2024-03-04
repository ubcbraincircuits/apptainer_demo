import suite2p
import os 

master_folder = "/mnt/data" #for apptainer
#master_folder = "data" #for local
# file =  "SHIFTED.tif"

master_folder = "/mnt/data"
file = "4"
filepath = os.path.join(master_folder, file)

#options
ops = suite2p.default_ops()

ops['batch_size'] = 2000 # we will decrease the batch_size in case low RAM on computer
ops['threshold_scaling'] = 2.0 # we are increasing the threshold for finding ROIs to limit the number of non-cell ROIs found (sometimes useful in gcamp injections)
ops['fs'] = 15 # sampling rate of recording, determines binning for cell detection
ops['tau'] = 1.25 # timescale of gcamp to use for deconvolution

db = {
    'data_path': [filepath],
}

output_ops = suite2p.run_s2p(ops=ops, db=db)