s = '''
import os\nimport uuid\nfrom flask import Flask, request, session, render_template, Markup\nfrom cat import cat\n\nflag = \"\"\napp = Flask(\n __name__,\n static_url_path='/', \n static_folder='static' \n)\napp.config['SECRET_KEY'] = str(uuid.uuid4()).replace(\"-\", \"\") + \"*abcdefgh\"\nif os.path.isfile(\"/flag\"):\n flag = cat(\"/flag\")\n os.remove(\"/flag\")\n\n@app.route('/', methods=['GET'])\ndef index():\n detailtxt = os.listdir('./details/')\n cats_list = []\n for i in detailtxt:\n cats_list.append(i[:i.index('.')])\n \n return render_template(\"index.html\", cats_list=cats_list, cat=cat)\n\n\n\n@app.route('/info', methods=[\"GET\", 'POST'])\ndef info():\n filename = \"./details/\" + request.args.get('file', \"\")\n start = request.args.get('start', \"0\")\n end = request.args.get('end', \"0\")\n name = request.args.get('file', \"\")[:request.args.get('file', \"\").index('.')]\n \n return render_template(\"detail.html\", catname=name, info=cat(filename, start, end))\n \n\n\n@app.route('/admin', methods=[\"GET\"])\ndef admin_can_list_root():\n if session.get('admin') == 1:\n return flag\n else:\n session['admin'] = 0\n return \"NoNoNo\"\n\n\n\nif __name__ == '__main__':\n app.run(host='0.0.0.0', debug=False, port=5637)
'''
list1 = s.split("\n")
print(list1)
for each in list1:
    if each == "":
        print(f"\t",end = "")
    else:
        print(each)



