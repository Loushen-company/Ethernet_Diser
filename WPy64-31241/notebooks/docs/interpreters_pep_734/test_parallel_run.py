import interpreters

from threading import Thread

import textwrap as tw

import time

def test_threading_interpreter():
    interp = interpreters.create()

    def t():
        interp.exec(tw.dedent("""
            import time
            for _ in range(50):
                print(end='.', flush=True)
                time.sleep(0.05)
            print("End of interp job")
        """))

    thread = Thread(target = t)
    print(f"Before thread.start(), {interp.is_running() = }")
    thread.start()
    time.sleep(1)
    print(f"After thread.start(), {interp.is_running()= }")
    thread.join()
    print(f"After thread.join(), {interp.is_running() = }")


if __name__ == "__main__":
    test_threading_interpreter()
