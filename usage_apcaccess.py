from apcaccess.status import get, print_status, parse

def main(host="localhost"):
    # apcupsdよりデータ取得
    raw = get(host=host)
    # rawデータだと文字化け
    print(raw)
    print("-"*10)

    # OrderedDictへparse
    parsed = parse(raw)
    print(parsed)

    # 読みやすい形でprint
    print_status(raw)
    print("-"*10)

if __name__ == "__main__":
    # ローカルホスト
    main()
    
    # リモートホスト
    # main(host="192.168.0.10")