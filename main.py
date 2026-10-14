#استدعاء المكاتب
from pywebio import *
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio import config
css = """

body {
    background-image: url('https://png.pngtree.com/thumb_back/fh260/background/20221224/pngtree-blue-musical-notes-background-image_1530362.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    margin: 0;
    padding: 20px;
}

li, a, span, details {
    display: block;
    width: fit-content;
    margin: 12px auto;
    color: #000000;
    background-color: #FFFFFF; 
    border: 1px solid #000000; 
    border-radius: 8px;
    padding: 20px 40px; 
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    text-align: center;
}

details { display: block; width: 


100%; margin: 12px auto; color: #000000; background-color: #FFFFFF; border: 1px solid #000000; border-radius: 8px; padding: 20px 40px; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3); text-align: center;

.plain-text {
    display: block;
    color: #FFFFFF !important;
    background: none !important;
    border: none !important;
    box-shadow: none !important;
    text-align: right;
    margin: 15px 0;
    padding: 0 !important;
}

"""
@config(css_style=css)

def rai2026():
    
    put_html("""

    <h3 id="h3">اغاني الراي 2026</h3>
    <p id="para">استمتع بسماعك للاغاني</p>
    <ul>
        <li>هنا تجد كل الاغاني التي تريد سماعها</li>

        <li>cheb bello</li>
        <li>cheb mourad</li>
        <li>cheb soufiane 31</li>
        <li>chaba warda</li>
        <li>cheb hichame smati</li>

    </li>

    <details id="y">

        <summary>cheb bello</summary>
        <p>L'3AYB FIHOM  اغنية</p>
                <audio controls>
                    <source src="https://mp3tourl.com/audio/1791987010297-957e49bb-4144-418b-9f9e-6f477d99e57a.mp3" type="audio/mp3">
                </audio>
                        <p>manich kima bekri اغنية </p>
                                <audio controls>
                                    <source src="https://mp3tourl.com/audio/1791989016746-9c50f72a-aa96-4c21-ae12-edf6b30fd804.mp3" type="audio/mp3">
                                </audio>
                                <p>Yahdrou اغنية </p>
                                        <audio controls>
                                            <source src="https://mp3tourl.com/audio/1791988388453-7d1f488e-9542-4876-bce8-67010378355a.mp3" type="audio/mp3">
                                        </audio>
                                                <p>3inehom Mesawsa 2020 Clip Officiel اغنية </p>
                                                        <audio controls>
                                                            <source src="https://mp3tourl.com/audio/1791986947425-593cedb2-0570-41e7-80a7-5be124cc7276.mp3" type="audio/mp3">
                                                        </audio>
        
    </details>
    <details id="y">
        <summary>cheb mourad</summary>
        <p> اغنية </p>
                <audio controls>
                    <source src="" type="audio/mp3">
                </audio>
                <p> اغنية </p>
                        <audio controls>
                            <source src="" type="audio/mp3">
                        </audio>
                        <p> اغنية </p>
                                <audio controls>
                                    <source src="" type="audio/mp3">
                                </audio>
                                <p> اغنية </p>
                                        <audio controls>
                                            <source src="" type="audio/mp3">
                                        </audio>
    </details>
    <details id="y">
        <summary>cheb cheb sofian 31</summary>
        <p> اغنية </p>
                <audio controls>
                    <source src="" type="audio/mp3">
                </audio>
                <p> اغنية </p>
                        <audio controls>
                            <source src="" type="audio/mp3">
                        </audio>
                        <p> اغنية </p>
                                <audio controls>
                                    <source src="" type="audio/mp3">
                                </audio>
                                <p> اغنية </p>
                                        <audio controls>
                                            <source src="" type="audio/mp3">
                                        </audio>
    </details>
    <details id="y">
        <summary>chaba warda</summary>
        <p> اغنية </p>
                <audio controls>
                    <source src="" type="audio/mp3">
                </audio>
                <p> اغنية </p>
                        <audio controls>
                            <source src="" type="audio/mp3">
                        </audio>
                        <p> اغنية </p>
                                <audio controls>
                                    <source src="" type="audio/mp3">
                                </audio>
                                <p> اغنية </p>
                                        <audio controls>
                                            <source src="" type="audio/mp3">
                                        </audio>
    </details>
    <details id="y">
        <summary>cheb hicham smati</summary>
        <p> اغنية </p>
                <audio controlاغنيةs>
                    <source src="" type="audio/mp3">
                </audio>
                <p> اغنية </p>
                        <audio controls>
                            <source src="" type="audio/mp3">
                        </audio>
                        <p> اغنية </p>
                                <audio controls>
                                    <source src="" type="audio/mp3">
                                </audio>
                                <p> اغنية </p>
                                        <audio controls>
                                            <source src="" type="audio/mp3">
                                        </audio>
    </details>
    <details id="y">
        <summary>cheb hicham tgv</summary>
    <p> اغنية </p>
            <audio controls>
                <source src="" type="audio/mp3">
            </audio>
            <p> اغنية </p>
                    <audio controls>
                        <source src="" type="audio/mp3">
                    </audio>
                    <p> اغنية </p>
                            <audio controls>
                                <source src="" type="audio/mp3">
                            </audio>
                            <p> اغنية </p>
                                    <audio controls>
                                        <source src="" type="audio/mp3">
                                    </audio>
    </details>
    <details id="y">
        <summary>cheb solking</summary>
        <p> اغنية </p>
                <audio controls>
                    <source src="" type="audio/mp3">
                </audio>
                <p> اغنية </p>
                        <audio controls>
                            <source src="" type="audio/mp3">
                        </audio>
                        <p> اغنية </p>
                                <audio controls>
                                    <source src="" type="audio/mp3">
                                </audio>
                                <p> اغنية </p>
                                        <audio controls>
                                            <source src="" type="audio/mp3">
                                        </audio>
    </details>
    <details id="y">
        <summary>cheb L'Algréno</summary>
        <p> اغنية </p>
                <audio controls>
                    <source src="" type="audio/mp3">
                </audio>
                <p> اغنية </p>
                        <audio controls>
                            <source src="" type="audio/mp3">
                        </audio>
                        <p> اغنية </p>
                                <audio controls>
                                    <source src="" type="audio/mp3">
                                </audio>
                                <p> اغنية </p>
                                        <audio controls>
                                            <source src="" type="audio/mp3">
                                        </audio>
    </details>
    <details id="y">
        <summary>cheb kadar japonais</summary>
        <p> اغنية </p>
                <audio controls>
                    <source src="" type="audio/mp3">
                </audio>
                <p> اغنية </p>
                        <audio controls>
                            <source src="" type="audio/mp3">
                        </audio>
                        <p> اغنية </p>
                                <audio controls>
                                    <source src="" type="audio/mp3">
                                </audio>
                                <p> اغنية </p>
                                        <audio controls>
                                            <source src="" type="audio/mp3">
                                        </audio>
    </details>
    <details id="y">
        <summary>cheb abdou gambitta</summary>
        <p> اغنية </p>
                <audio controls>
                    <source src="" type="audio/mp3">
                </audio>
                <p> اغنية </p>
                        <audio controls>
                            <source src="" type="audio/mp3">
                        </audio>
                        <p> اغنية </p>
                                <audio controls>
                                    <source src="" type="audio/mp3">
                                </audio>
                                <p> اغنية </p>
                                        <audio controls>
                                            <source src="" type="audio/mp3">
                                        </audio>
    </details>
    <details id="y">
        <summary>cheb bilal sghir</summary>
        <p> اغنية </p>
                <audio controls>
                    <source src="" type="audio/mp3">
                </audio>
                <p> اغنية </p>
                        <audio controls>
                            <source src="" type="audio/mp3">
                        </audio>
                        <p> اغنية </p>
                                <audio controls>
                                    <source src="" type="audio/mp3">
                                </audio>
                                <p> اغنية </p>
                                        <audio controls>
                                            <source src="" type="audio/mp3">
                                        </audio>
    </details>
    <details id="y">
        <summary>cheb djalil palermo</summary>
        <p> اغنية </p>
                <audio controls>
                    <source src="" type="audio/mp3">
                </audio>
                <p> اغنية </p>
                        <audio controls>
                            <source src="" type="audio/mp3">
                        </audio>
                        <p> اغنية </p>
                                <audio controls>
                                    <source src="" type="audio/mp3">
                                </audio>
                                <p> اغنية </p>
                                        <audio controls>
                                            <source src="" type="audio/mp3">
                                        </audio>
    </details>
    <p class="plain-text">ملاحظة:بعض الاغاني لم تتوفر بعد</p>
    <hr>
    <p class="plain-text">جميع الحقوق محفوظة @YOUCEFBISSAR</p>
    <script>document.title = "rai2026";</script>
""").style("direction:rtl; text-align:right;")
import os
if name == 'main': port = int(os.environ.get("PORT", 8080)) start_server(rai2026, host='0.0.0.0', port=port)
