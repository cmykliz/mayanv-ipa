# Transcriber
import sys
sys.path.insert(0, "epitran-mayan/epitran") # modify as needed

import epitran
print(epitran.__file__) # make sure it's imported correctly

mayan_g2p = epitran.Epitran('myn-Latn')

def transcribe_file(filename):
    lines_ipa = []
    filename_ipa = filename + '_ipa'
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            line = line.rstrip('\n')
            mayan_g2p.transliterate(line)
            lines_ipa.append(line)

    with open(filename_ipa, "w", encoding="utf-8") as f_out:
        f_out.write("\n".join(lines_ipa))

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python transcriber.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    transcribe_file(filename)
    print(f"Transcribed {filename} -> {filename}_ipa")