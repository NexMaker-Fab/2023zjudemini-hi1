<style>
    .custom-title {
        font-family: "Arial", sans-serif;
        font-size: 2.5em;
        text-align: center;
        padding: 10px 0;
        color: #EFEFEF;
        border-bottom: 3px solid #FF6347;
        margin-bottom: 20px;
    }
</style>

<div class="custom-title">Interface Applicantion Programming</div>

# Introduction to Processing
Processing is a flexible software sketchbook and a language for learning how to code. Since 2001, Processing has promoted software literacy within the visual arts and visual literacy within technology. There are tens of thousands of students, artists, designers, researchers, and hobbyists who use Processing for learning and prototyping.[Processing](https://processing.org/)
## Similar Tools
# Use Processing to make a simple game

```Processing
void setup() {
  size(300, 400);
}

int gameState = 0;
int score = 0;
float counter;
float cps;

void draw() {
  background(255,192,203);
  noStroke();
  int c = 50+(score*2);
  fill(0, 100, 255, c);
  ellipse(150, 200, 275, 275);
  if (gameState == 0) {
    textAlign(CENTER, CENTER);
    fill(240);
    textSize(40);
    text("Click to start", 150, 200);
    if (mousePressed) {
      gameState = 1;
      counter = 0;
      score = 0;
    }
  }
  if (gameState == 1) {
    counter=counter+0.0183;
    textAlign(CENTER, CENTER);
    fill(240);
    textSize(200);
    text(score, 150, 200);
    textSize(45);
    fill(200);
    text(counter, 150, 375);
    textSize(25);
    text("Press Any Key to Restart", 150, 25);
    if (counter > 10) {
      gameState = 2;
    }
    if (keyPressed) {
      gameState = 0;
    }
  }
  if (gameState == 2) {
    textAlign(CENTER, CENTER);
    fill(240);
    textSize(200);
    text(score, 150, 200);
    textSize(20);
    fill(240);
    text("Clicks Per Second (CPS):", 150, 355);
    textSize(25);
    text("Press Any Key to Restart", 150, 25);
    cps = score/10;
    text(cps, 150, 385);
    if (keyPressed) {
      gameState = 0;
      counter = 0;
      score = 0;
    }
  }
}

void mouseReleased() {
  if (gameState == 1) {
    score++;
  }
}
```
![Alt text](../_media/pro05_processing/game2.gif)
# Arduino and Processing
In this work, we did one demo in Processing and Arduino, which can communicate with each other.
Potentiometer controls the size of circle in Processing. This case is based on the Potentiometer, and the circle in Processing is controlled to change size from small to big through arduino output signal, so as to realize the interaction between software.
![Alt text](../_media/pro05_processing/arduino_processing.gif)
In arduino, the Gao Diping signal in human pyroelectric sensor is transmitted through serial port.
![Alt text](../_media/pro05_processing/arduino_cir.jpg)

```Arduino
int size = 0;
void setup() {
  Serial.begin(9600);
}
void loop(){
  size = map(analogRead(A0),0,1023,5,190);
  Serial.write(size);
//delay(10);
}

```

Import the Serial library in Processing to accept the serial signal transmitted by arduino. Set the screen size and serial port information in setup. Then set the size of the circle according to the signal and draw the circle. In the actual picture, there will be an animation of the circle size changing.

```Processing
import processing.serial.* ;
Serial port;

int diam = 50;

void setup() {
  size(400,400);
  background (#ffffff);
  
  fill(#48CFAD);
  noStroke();
  ellipse(200,200,diam,diam);
   for (int i = 0; i < Serial.list().length; i++) println("[", i, "]:", Serial.list()[i]);
  String portName = Serial.list()[Serial.list().length-1];//check the printed list
  //String portName = Serial.list()[0]; //For windows PC
  port = new Serial(this, portName, 9600);
  port.bufferUntil('\n'); // arduino ends each data packet with a carriage return 
  port.clear();   

}

void draw() {

  while(port.available()>0)
  {
    diam = port.readChar();
    // println(diam);
    clear();
    background (#ffffff);
    ellipse(200,200,diam,diam);
  }
  
    //println(777);
    //delay(100);
}
```