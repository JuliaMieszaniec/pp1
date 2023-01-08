class eBOOK():
    def __init__(self):
        self.work=False
        self.title="The Catcher in the Rye"
        self.author="J.D. Salinger"
        self.number_of_pages=304
        self.start_page=1
        
    def open(self):
        self.work=True

    def close(self):
        self.work=False

    def skip_to(self, x):
        if self.work==True:
                self.start_page=1
                self.start_page=+x
        else:
            print("Sorry, the eBook is closed")
        
    
    def ebook_status(self):
        if self.work==True:
            print(f"We read {self.title} writtten by {self.author}. Current page is {self.start_page}.")
        else:
            print("the eBook is closed")


eb=eBOOK()
eb.ebook_status()
eb.open()
eb.ebook_status()
eb.skip_to(4)
eb.ebook_status()
eb.close()
eb.skip_to(7)