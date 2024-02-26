import pygame 

class Lubo:
    def __init__(self):
        super().__init__()
        self.verbose = True 
        self.run_flag = True
        self.upscale = 5
        self.screen_width = 128 * self.upscale
        self.screen_height = 64 * self.upscale
        self.setup_display()
        self.clock = pygame.time.Clock()


        
    def report(self, msg):
        if self.verbose:
            print("[Lubo] " + msg)


    def setup_display(self):
        self.report(f"Upscale: {str(self.upscale)}")
        self.report(f"Display resolution: {str(self.screen_width)}x{self.screen_height}")
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

    def show(self):
        pygame.display.flip()

    def clear(self):
        self.screen.fill('black')

    def pixel(self, x, y):
        p = self.upscale
        size = self.upscale
        rect = pygame.Rect(x, y, 10, 10)
        pix = pygame.draw.rect(self.screen, 'white', rect)
        return rect

    def run(self):
        while self.run_flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_flag = False
            pix = self.pixel(10, 30)

            i = 1

            if i == 99:
                i = 0
            pix.move(i, 30)
            i += 1


            self.show()
            self.clock.tick(60)


l = Lubo().run()