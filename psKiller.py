import pikepdf
import argparse

parser = argparse.ArgumentParser(
    prog = 'psKiller',
    description = 'PDF password remover'
)

parser.add_argument('filepath', metavar = 'filepath', type = str, help = 'path to file')
parser.add_argument('password', metavar = 'password', type = str, help = 'password')

args = parser.parse_args()

def psKiller(filepath, password):
    pdf = pikepdf.open(filepath, password=password, allow_overwriting_input=True)
    pdf.save(filepath)

psKiller(args.filepath, args.password)

