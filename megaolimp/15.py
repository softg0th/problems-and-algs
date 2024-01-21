import re


def clear(code):
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    code = re.sub(r'//.*', '', code)
    code = list(code)
    clear_code = []
    start_text = False

    while code[-1] in (' ', '\n'):
        code.pop()
    for char in code:
        if not start_text:
            if char not in (' ', '\n'):
                clear_code.append(char)
                start_text = True
        else:
            clear_code.append(char)

    return ''.join(clear_code)


def interface():
    code = '''
    /*
 * My first ever program in Java!
 */
class Hello { // class body starts here

 /* main method */
  public static void main(String[] args/* we put command line arguments here*/) {
    // this line prints my first greeting to the screen
    System.out.println("Hi!"); // :)
  }
} // the end
// to be continued...
    '''
    output = clear(code)
    print(output)


if __name__ == '__main__':
    interface()

