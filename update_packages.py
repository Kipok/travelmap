import subprocess

def update_packages(req_file):
    print(f"Reading {req_file}")
    with open(req_file, 'rt', encoding="utf-8") as fin:
        lines = fin.readlines()
    
    with open(req_file, 'wt', encoding='utf-8') as fout:
        for line in lines:
            package, version = line.split('==')
            output = subprocess.run(f"pip index versions {package}", shell=True, check=True, capture_output=True)
            version = output.stdout.decode().split("Available versions:")[1].split()[0].split(',')[0].strip()
            to_write = f"{package}=={version}"
            print(to_write)
            fout.write(to_write + "\n")


if __name__ == '__main__':
    update_packages('dev_requirements.txt')
    update_packages('prod_requirements.txt')

