import string
from methods.vigenere import VigenereEncoder
from methods.ceasar import CeasarEncoder
from methods.polybios import PolybiosEncoder
from methods.skytala import Skytala

# --------------- Vigenere ----------------
message = "sehr_viel_uebungsspass_ohne_ende"
key = "lehrreich"
alphabet = string.ascii_lowercase
alphabet = alphabet + "_"

vigEncoder = VigenereEncoder(message=message, key=key, alphabet=alphabet)
print(vigEncoder.encrypt())


# --------------- Ceasar ----------------
message = "Ohil ubu, hjo! Wopsvzvwopl," \
          "Qbypzalylp buk Tlkpgpu, Buk" \
          "slpkly hbjo Aolvsvnpl! Kbyjohbz" \
          "zabkplya, tpa olpzzlt Iltblou." \
          "Kh zalo pjo ubu, pjo hytly Avy!" \
          "Buk ipu zv rsbn, hsz dpl gbcvy."
k = 7
alphabet = string.ascii_lowercase
cesEncoder = CeasarEncoder(message=message, k=k, alphabet=alphabet)

print(cesEncoder.decrypt())

# --------------- Polybios ----------------

message = "5315431132321551151251342215342215532444441534" \
          "2311214512151143121524451545244445121544441543" \
          "1151211424153132115144514352354312154315244515" \
          "45113244251534151424151411443424132345455134"

polybiosEncoder = PolybiosEncoder(message=message)
print(polybiosEncoder.decrypt())


# --------------- Skytala ----------------

message = "VERSCHLUESSELNMACHTGROSSENSPASS"
k = 5
skytala = Skytala(message, k , "xyz")
print(skytala.encrypt())