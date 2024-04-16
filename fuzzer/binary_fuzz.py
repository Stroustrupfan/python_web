import os
import subprocess

binary_files = "../Dataset/SC_Bin_test"

for file in os.listdir(binary_files):
    file_path = os.path.join(binary_files, file)

    command_for_afl = ["afl-fuzz", "-i", "input_dir", "-o", "output_dir", file_path]
    subprocess.run(command_for_afl)