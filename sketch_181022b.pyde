def setup():
    size(1154,500)
    
x = 0   
y = 0 
def draw():
    global x
    global y
    noStroke()
    
    if x >= 1150:
        x = 0
    if y >= 1000:
        y = 0
    background(135,206,250)
    x += 5
    y += 4
    
    fill(255,255,0)
    ellipse(1154,0,200,200)

    fill(169)
    ellipse(x ,165,100,50)
    ellipse(x ,145,50,50)
    fill(30,144,255)
    triangle(x,180,x - 100,250,x + 100,250)
    
    fill(255)
    ellipse(954,250,50,50)
    ellipse(945,235,50,50)
    ellipse(977,230,50,50)
    ellipse(925, 245 ,50, 50)

    ellipse(30,250-155,50,50)
    ellipse(25,250-125,50,50)
    ellipse(50,250-140,50,50)
    ellipse(55,250-175,50,50)

    ellipse(535,250-75,50,50)
    ellipse(525,250-50,50,50)
    ellipse(550,250-35,50,50)
    ellipse(560,250-55,50,50)
    
    ellipse(285,265,50,50)
    ellipse(265,265,50,50)
    ellipse(295,240,50,50)
    ellipse(310,270,50,50)
    
    fill(34,139,34)
    rect(0,350,1154,400)
    
    fill(222,184,135)
    rect(300,415,50,50)
    
    rect(385,430,50,50)
    
    rect(480,355,50,50)
    
    rect(450,445,50,50)
    
    rect(425,375,50,50)
    
    rect(540,410,50,50)
    
    fill(139,69,19)
    triangle(300,415,325,395,350,415)
    
    triangle(385,430,410,410,435,430)
    
    triangle(480,355,505,335,530,355)
    
    triangle(450,445,475,425,500,445)
    
    triangle(425,375,450,355,475,375)
    
    triangle(540,410,565,390,590,410)
    
    fill(0,100,0)
    ellipse(850,435,100,35)
    rect(800,412,100,25)
    ellipse(850,420,50,50)
    
    stroke(1)
    strokeWeight(4)
    line(785,375,835,400)
    
    noStroke()
    fill(0,100,0)
    ellipse(1000,400,100,35)
    rect(950,377,100,25)
    ellipse(1000,385,50,50)
    
    stroke(1)
    strokeWeight(4)
    line(935,350,985,365)
    
    noStroke()
    fill(0,100,0)
    ellipse(700,415,100,35)
    rect(650,392,100,25)
    ellipse(700,400,50,50)

    stroke(1)
    strokeWeight(4)
    line(635,350,685,380)
