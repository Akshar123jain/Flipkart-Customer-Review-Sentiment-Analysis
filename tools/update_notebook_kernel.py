import json
p = r"Notebook/sentiment_analysis.ipynb"
with open(p, 'r', encoding='utf-8') as f:
    d = json.load(f)
meta = d.get('metadata', {})
meta['kernelspec'] = {'name':'filpkart','display_name':'Python (filpkart)','language':'python'}
d['metadata'] = meta
with open(p, 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=4)
print('updated', p)
