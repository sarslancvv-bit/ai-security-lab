NOTES:
-----------------------------
' are literal string will print what is inside.

" will not substitute varible values whereas " delimited strings will.

Example code:

foo=bar
echo "$foo"
-bar
echo '$foo'
-$foo
----------------------
if, case, while and for are also used in bash.

Similarly, bash has functions that takes arguments and can operate with them.

Example:

mcd () {
    mkdir -p "$1"
    cd "$1"
}
mcd () → creates a function named mcd
$1 → the first argument you give the function 
mkdir -p "$1" → creates that directory; -p also creates missing parent directories and doesn't complain if it already exists
cd "$1" → moves into that directory
"$1" is quoted so names containing spaces work correctly

executable olduğu zaman (yani x)-- ls fonksiyonunda yeşil gözükür dosya. 

1- nano myscript.sh yazıp- text editorü açtım içine "ls" yazıp kaydettim."

2- sudo chmod +x myscript.sh yaptım- permission verdim dosyaya execute etmesi için "-rwxr-xr-x 1 samim samim    3 Aug 17 20:28 myscript.sh"

3- ./myscript.sh - Bu da direkt sanki terminale ls yazıp çalıştırmışım gibi davrandı zaten "ls" print etmesini istemiştim.

4- cat myscript.sh yazınca direk - ls output etti.

5- ls ve pwd altına ekledim- istediğimi yukarıdan aşağı yaptı.


-----------------------------
&& - and demek bashte

|| - veya demek bashte

echo "Bugün: $(date)"

ilk bash "date" i çalıştırır.

output: Bugün: Mon Aug 17 20:30:00 +03 2026, mesela.
----------------------------------------------------

$(komut):
Komutun çıktısını metin olarak getir.

<(komut) ise kabaca:
Komutu çalıştır ve çıktısını bir dosya gibi sun.

diff <(ls foo) <(ls bar)

Ama diff normalde iki dosya ister:
diff file1.txt file2.txt
Biz elimizde gerçek dosyalar olmadan iki komutun çıktısını karşılaştırmak istiyoruz.
Bash <(...) sayesinde bu çıktıları geçici olarak dosya benzeri şeylere bağlar.

Bunun gibi:
ls foo > temp1
ls bar > temp2
diff temp1 temp2

Ama Bash bunu bizim için otomatik yapar.
Gerçekte Linux üzerinde bazen şöyle yollar oluşturabilir:
/dev/fd/63
/dev/fd/62
---------------------
#!/bin/bash
Buna shebang denir --- Bu satır işletim sistemine şunu söyler:
"Bu dosyayı Bash interpreter kullanarak çalıştır."

Örneğin script'in adı:
example.sh

Dosyayı executable yaptıysan:
chmod +x example.sh

sonra
./example.sh -- yapabilirsin

Linux ilk satıra bakar:
#!/bin/bash
ve script'i Bash ile çalıştırır.

/bin/bash example.sh -- gibi davranır.
-----------------------

echo "Running program $0 with $# arguments with pid $$"

$0 - çalıştırlan scriptin adıdır. (mesela - ./example.sh)

$# - scripte verilen argüman sayısıdır:

mesela - ./example.sh a.txt b.txt c.txt - 3 argument var - output=3

$$ - çalıştırılan Bash process'in PID'sidir.

mesela - echo $$ - 42351- ID numarasını printler.

bu arada mesela: $1 'in outputu - a.txt'dir 

veya $2' nin outputu - b.txt' dir - bash yukarıdan aşağı okur. ve numaralandırır.

$@ - scriptte verilen bütün argumentleri temsil eder. 

mesela- ./example.sh a.txt b.txt c.txt - "$@" - çıktısı: "a.txt" "b.txt" "c.txt"

for file in "$@"; do

Bana verilen bütün argümanları sırayla gez ve her seferinde mevcut argument'e file
isimli değişkeni koy:

file="a.txt"
file="b.txt"
file="c.txt"

for ...; do
    commands   ---> bash mantığı böyledir,python'daki for file in files gibi
done

grep foobar "$file"- grep text veya pattern aramak için kullanılır.

mesela: a.txt'nin içinde -hello world foobar apple

her birinde iterate edip "foobar" arar. bulursa status=0 yani başaralı bulamazsa 0'dan farklı bir sayı çevirir - hata / başarısızlık / özel durum

grep foobar a.txt
echo $? - önceki komutun exit status'ünü basar.

mesela başarılıysa - 0 basar, bulunmadıysa 1 basar.

Kısaca: 
grep foobar "$file"
if [[ $? -ne 0 ]]; then   --grep'i çalıştır. Sonra grep'in başarılı olup olmadığına bak.

Linuxta dev/null- özel bir dosya (kara delik gibi)- içine atılan her şey kaybolur.

echo "hello" > /dev/null - sonuçta terminalde hiç bir şey yazmaz.

hello dev/null' un içine gönderildi ve kayboldu.

command > file.txt - echo hello > test.txt bunun gibi:
terminalde hello yazmaz. test.txt de hello olur.

STDOUT ve STDERR nedir?
Unix/Linux'ta programların standart olarak üç önemli stream'i vardır:
0 = STDIN
1 = STDOUT
2 = STDERR

STDIN — 0
Programın input aldığı yer.
Örneğin keyboard.

STDOUT — 1
Programın normal output verdiği yer.
Örneğin:
echo hello

STDERR — 2
Programın hata mesajlarını gönderdiği yer.
Örneğin:
ls nonexistent.txt- hata mesajı verir.

2> /dev/null - buradaki 2' sayısı STDERR demek.

kısaca bu kod - Hata mesajlarını da çöpe at. demek

bash' te [[.....]], condition kontrolü yapmak için kullanılır.

[[ $? -ne 0 ]]

-ne - not equal demek.
Önceki komutun exit status'ü 0'a eşit değil mi?

eğer eşit değilse condition "true" olur.

bashte sayı karşılaştırmaları:
-eq → equal
-ne → not equal
-lt → less than
-le → less than or equal
-gt → greater than
-ge → greater than or equal

-fi , "if condition" kapatmak için kullanılır yapı şu şekilde:
if [[ condition ]]; then
    commands
fi

echo "# foobar" >> "$file"

file.txt:
hello
world

">" - bu işaret dosyanın önceki içeriğini siler ve yeniden yazar.

mesela: echo "apple" > file.txt

apple

apple kalır, eski içerik gider.

">>" - dosyanın sonuna ekler. 

mesela: echo "apple" >> file.txt

hello
world
apple
----------------------

Wildcards - Whenever you want to perform some sort of wildcard matching, you can use ? and * to match one or any amount of characters respectively. For instance, given files foo, foo1, foo2, foo10 and bar, the command rm foo? will delete foo1 and foo2 whereas rm foo* will delete all but bar.

Curly braces {} - Whenever you have a common substring in a series of commands, you can use curly braces for bash to expand this automatically. This comes in very handy when moving or converting files.  
Examples:

convert image.{png,jpg}
# Will expand to
convert image.png image.jpg

cp /path/to/project/{foo,bar,baz}.sh /newpath
# Will expand to
cp /path/to/project/foo.sh /path/to/project/bar.sh /path/to/project/baz.sh /newpath

# Globbing techniques can also be combined
mv *{.py,.sh} folder
# Will move all *.py and *.sh files
-------------------------
SHELL TOOLS:

finding files:
# Find all directories named src
find . -name src -type d
# Find all python files that have a folder named test in their path
find . -path '*/test/*.py' -type f
# Find all files modified in the last day
find . -mtime -1
# Find all zip files with size in range 500k to 10M
find . -size +500k -size -10M -name '*.tar.gz'
# Delete all files with .tmp extension
find . -name '*.tmp' -exec rm {} \;
# Find all PNG files and convert them to JPG
find . -name '*.png' -exec magick {} {}.jpg \;

find . -iname (case-sensetive'i kaldırır)

locate uses a database that is updated using updatedb. In most systems, updatedb is updated daily via cron. 

Therefore one trade-off between the two is speed vs freshness. 

Moreover find and similar tools can also find files using attributes such as file size, modification time, or file permissions, while locate just uses the file name.

most UNIX-like systems provide grep, a generic tool for matching patterns from the input text. grep is an incredibly valuable shell tool

Some frequently use are -C for getting Context around the matching line and -v for inverting the match, i.e. print all lines that do not match the pattern. 
For example, grep -C 5 will print 5 lines before and after the match. 

When it comes to quickly searching through many files, you want to use -R since it will Recursively go into directories and look for files for the matching string.

# Find all python files where I used the requests library
rg -t py 'import requests'
# Find all files (including hidden files) without a shebang line
rg -u --files-without-match "^#\!"
# Find all matches of foo and print the following 5 lines
rg foo -A 5
# Print statistics of matches (# of matched lines and files )
rg --stats PATTERN
-----------------------------

Asıl önemli olan: Pipe |
Buradaki ana fikir |:
A | B | C
şu mantıktadır:
A'nın çıktısını B'ye ver → B'nin çıktısını C'ye ver.

Bu yüzden shell'de küçük komutları LEGO parçaları gibi birbirine bağlayabilirsin.

grep "aranacak_kelime" dosya:

Eşleşmeyenleri göster: -v
grep -v "INFO" server.log
Yani:
INFO içermeyen satırları göster.


Satır numarası: -n
grep -n "ERROR" server.log
Çıktı:
3:ERROR Database connection failed
5:ERROR Timeout occurred

grep "payment failed" application.log
Örneğin ödeme sisteminde hangi satırlarda ödeme hatası olmuş görebilirsin.

Case-insensitive: -i
grep -i "error" server.log
Şunların hepsini eşleştirebilir:
ERROR
error
Error

grep "ERROR" server.log
Çıktı:
ERROR Database connection failed
ERROR Timeout occurred
Yani grep:
Bana sadece ERROR geçen satırları göster.


Normalde:
grep ERROR server.log
çıktıyı terminalde görürsün.
Ama:
grep ERROR server.log > errors.txt
dersen terminal yerine errors.txt içine yazılır.
Sonuç:
errors.txt
içinde:
ERROR Database connection failed
ERROR Timeout occurred

">>"  - Dosyanın sonuna eklemek

">"   overwrite
">>"  append

curl: İnternetten veri almak

curl shell’den HTTP isteği yapmanı sağlar.

curl https://example.com

Bu siteye GET isteği yollar ve cevabı terminale basar.

Gerçek hayatta asıl önemli kullanım API’lerdir.

Örneğin API sana şöyle JSON dönsün:
{
  "name": "Alice",
  "age": 28,
  "city": "London"
}

Şunu yaparsın:
curl https://api.example.com/user
ve JSON terminalde görünür.
-----------------------------
curl + redirect

API’den gelen cevabı dosyaya kaydet:
curl https://api.example.com/user > user.json

Artık:
user.json
içinde API cevabı var.

Örneğin:
curl https://api.company.com/orders > orders.json
Sonra bu veri analiz edilir.

curl -o

yukarıdaki işin aynısını yapar:

curl -o user.json https://api.example.com/user

-o output file demek

yani user.json olarak kaydet.

jq: JSON verisini işlemek

jq, JSON için adeta grep gibi düşünebilirsin.

Diyelim:
{
  "name": "Alice",
  "age": 28,
  "city": "London"
}

dosyan: user.json

jq '.name' user.json --> "Alice"

jq '.age' user.json --> "28"

jq '.city' user.json --> "London"

en önemli kombinasyonlardan:

curl | jq  :

curl https://api.example.com/user | jq '.name'

API
 ↓
curl
 ↓
JSON
 ↓
jq '.name'
 ↓
"Alice"
-------------------------
API ın cevabı:

[
  {
    "name": "Alice",
    "salary": 5000
  },
  {
    "name": "Bob",
    "salary": 6000
  },
  {
    "name": "Charlie",
    "salary": 4500
  }
]

jq '.[].name' employees.json -- "[]" array elemanlarını tek tek gez demek.

Sonuç:
"Alice"
"Bob"
"Charlie"
------------------------
jq ile filtreleme:

jq '.[] | select(.salary > 5000)' employees.json

Sonuç: 
{
  "name": "Bob",
  "salary": 6000
}

sadece isim istiyorsan:
jq '.[] | select(.salary > 5000) | .name' employees.json

Sonuç: "Bob"

Burada dikkat et: jq'nun kendi içinde de | kullanımı vardır. Bu shell pipe değildir; jq filter syntax’ıdır.
---------------------
Gerçek iş senaryosu: API’den aktif kullanıcıları almak

API cevabı:
[
  {"name":"Alice","active":true},
  {"name":"Bob","active":false},
  {"name":"Charlie","active":true}
]

curl https://api.company.com/users | jq '.[] | select(.active
== true) | .name'
Sonuç:
"Alice"
"Charlie"
Gerçek bir DevOps/data/backend ortamında bu tarz komutlar çok yaygındır.
--------------------
sed: Metinde hızlı değiştirme

sed daha çok:
Bir metinde bir şeyi başka bir şeyle değiştir.

Örnek dosya:
Hello Alice
Alice is an engineer

Şunu çalıştır:
sed 's/Alice/Bob/' file.txt
Çıktı:
Hello Bob
Bob is an engineer

Buradaki:
s/Alice/Bob/

mantığı:
substitute Alice with Bob
Yani:
Alice → Bob
-----------------------
sed -i: Dosyayı gerçekten değiştirmek

Normal:
sed 's/foo/bar/' file.txt
sadece sonucu terminale basar.

Dosyayı kalıcı değiştirmek için çoğu Linux sisteminde:
sed -i 's/foo/bar/g' file.txt
Buradaki g:
Satır içindeki bütün eşleşmeleri değiştir.

Örneğin:
foo foo foo
→
bar bar bar
-----------
awk: Sütunlarla çalışmak
awk başlangıçta biraz garip görünür ama çok güçlüdür.
Diyelim employees.txt:
Alice 5000 Engineering
Bob 6000 Finance
Charlie 4500 Marketing
Burada sütunlar var.
Birinci sütunu almak için:
awk '{print $1}' employees.txt
Sonuç:
Alice
Bob
Charlie
İkinci sütun:
awk '{print $2}' employees.txt
Sonuç:
5000
6000
4500
Burada:
$1 → birinci sütun
$2 → ikinci sütun
$3 → üçüncü sütun
----------------------
awk ile condition
5000’den fazla kazanan:
awk '$2 > 5000 {print $1}' employees.txt
Sonuç:
Bob
Yani:
İkinci sütun 5000’den büyükse birinci sütunu yazdır.
-------------------------
grep
→ "Hangi satırda bu kelime var?"

sed
→ "Bu kelimeyi başka kelimeyle değiştir."

awk
→ "Bu satırdaki 2. sütunu al ve hesaplama yap."

Örneğin:
grep ERROR server.log
→ ERROR satırlarını bul.
sed 's/ERROR/WARNING/' server.log
→ ERROR yazılarını WARNING yap.
awk '{print $1}' server.log
→ Her satırın ilk sütununu göster.
----------------
Diyelim bir API’den çalışan bilgileri alıyorsun:
curl https://api.company.com/employees
JSON geliyor.
Aktif çalışanları seç:
curl https://api.company.com/employees |
jq '.[] | select(.active == true)'
Sadece isimleri al:
curl https://api.company.com/employees |
jq -r '.[] | select(.active == true) | .name'
Dosyaya kaydet:
curl https://api.company.com/employees |
jq -r '.[] | select(.active == true) | .name' \
> active_users.txt
Artık:
active_users.txt
şöyle olabilir:
Alice
Charlie
David
Sonra kaç kişi var?
cat active_users.txt | wc -l
Örneğin:
3
Bu tam anlamıyla gerçek iş dünyasındaki shell mantığıdır:
VERİYİ AL
    ↓
curl

VERİYİ FİLTRELE
    ↓
jq / grep

GEREKİRSE DÖNÜŞTÜR
    ↓
sed / awk

DOSYAYA YAZ
    ↓
>

SONRA BAŞKA İŞLEM YAP