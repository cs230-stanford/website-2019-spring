import glob, os
from tqdm import tqdm
from PyPDF2 import PdfFileWriter, PdfFileReader

def delete_cover(fn, indir, outdir):
    infile = PdfFileReader(f'{indir}/{fn}', 'rb')
    outfile = PdfFileWriter()
    num_pages = infile.getNumPages()

    for i in range(1, num_pages):
        page = infile.getPage(i)
        outfile.addPage(page)

    with open(f'{outdir}/{fn}', 'wb') as f:
        outfile.write(f)

fns = glob.glob('posters_orig/*.pdf')
print(f'Total poster PDFs to convert: {len(fns)}')
for fn in tqdm(fns):
    delete_cover(os.path.basename(fn), 'posters_orig', 'posters')
print(f'Finished!')

fns = glob.glob('reports_orig/*.pdf')
print(f'Total report PDFs to convert: {len(fns)}')
for fn in tqdm(fns):
    delete_cover(os.path.basename(fn), 'reports_orig', 'reports')
print(f'Finished!')
