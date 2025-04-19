from flask import Flask , send_file

app = Flask(__name__)

app_name = "My Application Name is: Farel aja"

#1 App Route Index Flask
@app.route("/")
def home():
    return "Hi, bang farel"

    #2 App Route di Route Aplikasi
    @app.route("/aplikasi")
    def aplikasi():
        return "<p>Ini adalah laman  aplikasi</p>"

        #3 App Route dengan HTML
        @app.route('/about')
        def about():
            return send_file('about_without_bostrapp.html')

            #4 App Route dengan HTML with bostrapp
            @app.route("/about-bostrapp")
            def about_bostrapp():
                return send_file('about.html')

                #5 App Route Dinamis
                @app.route('/pesan/<string:pesan>')
                def getnama(pesan):
                    return "untukmu 2000 tahun yang lalu: {}".format(pesan)

                    #6 App Route ID
                    @app.route('/nim/<int:nim>')  # Hanya menerima angka
                    def nim(nim):
                        return f"NIM MAHASISWA: {nim}"

                        #7 App Route Variabel Global
                        @app.route('/variabel-global/')
                        def variabel_global():
                            return f"selamat membaca {app_name}"

                            #8 App Route Dictionary Variabel
                            @app.route('/data')
                            def data():
                                user = {"name": "farel", "age": 18, "city": "Bantaeng "}
                                return send_file('data.html', user=user)

                            if __name__ == "__main__":
                                        app.run(debug=True)