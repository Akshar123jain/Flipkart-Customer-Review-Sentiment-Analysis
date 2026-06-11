import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError
import sys
p_in = 'Notebook/sentiment_analysis.ipynb'
p_out = 'output/sentiment_analysis_executed.ipynb'
nb = nbformat.read(p_in, as_version=4)
client = NotebookClient(nb, timeout=600, kernel_name='filpkart', cwd='Notebook')
try:
    client.execute()
    nbformat.write(nb, p_out)
    print('Executed and saved to', p_out)
except CellExecutionError as e:
    print('Execution failed:', e)
    sys.exit(1)
