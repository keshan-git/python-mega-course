from flask import Flask, render_template
from generator import generate

app = Flask(__name__)


@app.route('/graph')
def route_graph():
    js_code, div_comp, js_file_paths, css_file_paths = generate()
    return render_template('graph.html', js_code=js_code, div_comp=div_comp, js_file_path=js_file_paths[0],
                           css_file_path=css_file_paths[0])


if __name__ == '__main__':
    app.run(debug=True, port='8080')
