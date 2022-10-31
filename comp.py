from jelly import dictionary
code_page = '''¡¢£¤¥¦©¬®µ½¿€ÆÇÐÑ×ØŒÞßæçðıȷñ÷øœþ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¶°¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ƁƇƊƑƓƘⱮƝƤƬƲȤɓƈɗƒɠɦƙɱɲƥʠɼʂƭʋȥẠḄḌẸḤỊḲḶṂṆỌṚṢṬỤṾẈỴẒȦḂĊḊĖḞĠḢİĿṀṄȮṖṘṠṪẆẊẎŻạḅḍẹḥịḳḷṃṇọṛṣṭụṿẉỵẓȧḃċḋėḟġḣŀṁṅȯṗṙṡṫẇẋẏż«»‘’“”'''

class Compress(list):
    def character(self, c):
        if c in '\n\x7f¶':
            o = 95
        elif ' ' <= c <= '~':
            o = ord(c)-32
        else:
            raise ValueError(c + " is neither printable ASCII nor a linefeed.")
        self += [lambda z: 3*z+0, lambda z: 96*z+o]; return self
    def string(self, s):
        for c in s: self.character(c)
        return self
    def dictionary(self, w):
        ts = bool(self)
        if w[:1] == ' ': w = w[1:]; ts = not ts
        dct = dictionary.short if len(w) < 6 else dictionary.long
        W, sc = (w, 0) if w in dct else (w[:1].swapcase() + w[1:], 1)
        if W not in dct: raise ValueError(w + " isn't in the dictionary.")
        f = ts or sc; j = (2 if sc else 1) if ts else 0; i = dct.index(W)
        self += [lambda z: 3*z+2, lambda z: 3*z+j] if f else [lambda z: 3*z+1]
        self += [lambda z: 2*z+int(len(w) < 6), lambda z: len(dct)*z+i]
        return self
    def go(self):
        compressed = []; z = 0
        for f in self[::-1]: z = f(z)
        while z:
            c = z % 250
            if c == 0: c = 250
            z = (z - c) // 250
            compressed.append(code_page[c - 1])
        return '“{0}»'.format(''.join(compressed[::-1]))
print(Compress()
  .dictionary("war")
  .string(" ")
  .dictionary("freedom")
  .string(" ")
  .dictionary("ignorance")
  .string(" ")
  .dictionary("strength")
  .string(" ")
  .dictionary("slavery")
  .string(" ")
  .dictionary("peace")
  .string(" ")
  .go()
)
#https://codegolf.stackexchange.com/questions/107937/war-is-peace-freedom-is-slavery-ignorance-is-strength