from collections import deque

class BrowserHistory:
    def __init__(self, max_size=5):
        self.history = deque(maxlen=max_size)
        self.forward_stack = deque()

    def add_new_page(self, url):
        if self.history and self.history[-1] == url:
            print(f"Already on {url}")
            return
        self.history.append(url)
        self.forward_stack.clear()
        print(f"Visited: {url}")
        self.print_state()

    def go_back(self):
        if len(self.history) <= 1:
            print("Cannot go back further.")
            return
        last_page = self.history.pop()
        self.forward_stack.append(last_page)
        print(f"Back to: {self.history[-1]}")
        self.print_state()

    def go_forward(self):
        if not self.forward_stack:
            print("No forward history.")
            return
        page = self.forward_stack.pop()
        self.history.append(page)
        print(f"Forward to: {page}")
        self.print_state()

    def print_state(self):
        print(f"History: {list(self.history)}")
        print(f"Forward Stack: {list(self.forward_stack)}\n")

browser = BrowserHistory()

browser.add_new_page("google.com")
browser.add_new_page("openai.com")
browser.add_new_page("github.com")
browser.add_new_page("stackoverflow.com")
browser.add_new_page("python.org")

browser.add_new_page("wikipedia.org")

browser.go_back()
browser.go_back()

browser.go_forward()

browser.add_new_page("news.ycombinator.com")
