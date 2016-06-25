from http.server import CGIHTTPRequestHandler, test
import os

def main():
    # http://stackoverflow.com/questions/11419572/how-to-set-the-documentroot-while-using-pythons-httpserver
    os.chdir(r"C:\apcupsd")

    # ディレクトリ名の前の`/`を付け忘れると正常に動作しない
    CGIHTTPRequestHandler.cgi_directories = ["/cgi"]

    test(HandlerClass=CGIHTTPRequestHandler, port=8080)

if __name__ == "__main__":
    main()