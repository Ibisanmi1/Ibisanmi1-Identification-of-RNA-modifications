original_json=open('data.json','r')
new_json=open('new_data.json','w')
for ln in original_json:
    new_json.write(ln.strip()+'\r\n')
new_json.close()