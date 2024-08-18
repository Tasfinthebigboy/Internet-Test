from flask import Flask, jsonify, render_template
import speedtest

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/speedtest')
def speed_test():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        st.download()
        st.upload()
        results = st.results.dict()
        return jsonify({
            'download': results['download'] / 1e6,  # Convert to Mbps
            'upload': results['upload'] / 1e6,  # Convert to Mbps
            'ping': results['ping']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5500, host="0.0.0.0")
