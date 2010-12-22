/**
 * Background Image. 
 * 
 * This example presents the fastest way to load a background image
 * into Processing. To load an image as the background, it must be
 * the same width and height as the program.
 */
 
BufferedReader reader;
PImage bg;
HashMap x_map, y_map;
String line;
String[] headers;
int step = 0;

void setup() 
{
  size(1046,453);
  frameRate(30);
  bg = loadImage("m4-map.png");
  reader = createReader("RTAData.csv");
  try {
    line = reader.readLine();
    headers = split(line, ",");
  } catch (IOException e) {
    e.printStackTrace();
    line = null;
  }
  
  x_map = initXMap();
  y_map = initYMap();
  
  ellipseMode(CENTER);
}

void draw() 
{
  background(bg);

  try {
    line = reader.readLine();
  } catch (IOException e) {
    e.printStackTrace();
    line = null;
  }

  if (line == null) {
    // Stop reading because of an error or file is empty
    noLoop();  
  } else {
    String[] pieces = split(line, ",");
    
    fill(255,255,255);
    for (int i = 1; i < pieces.length; i++)
    {
      int x = (Integer)x_map.get(headers[i]);
      int y = (Integer)y_map.get(headers[i]);
      float time = float(pieces[i]);
      int r = int(time / 100.0);
//      println(i + " " + x + " " + y + " " + time);
      ellipse(x, y, r+1, r+1);
    }
  }
  
  fill(0);
  text(step, 20, 420);
  step++;
}
