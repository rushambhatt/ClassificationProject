import numpy as np
import mne

# location of sample data
sample_data_folder = "/Users/rusham/Downloads/files"
sample_data_file = f"{sample_data_folder}/S001/S001R01.edf"

# read the raw data
raw = mne.io.read_raw_edf(sample_data_file)

raw.compute_psd(fmax=30).plot(picks="data", exclude="bads", amplitude=False)
raw.plot(duration=5, n_channels=30)