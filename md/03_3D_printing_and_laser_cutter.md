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

<div class="custom-title">3D Printing And Laser Cutter</div>

# Introduction
**3D printing (3DP)** is a type of rapid prototyping technology, also known as additive manufacturing , which is a technology based on a digital model file, the use of powdered metal or plastic and other bondable materials, by printing layer by layer to construct objects.

3D printing is usually realized using digital technology material printers. It is often used to make models in the fields of mold making and industrial design, and is gradually used in the direct manufacturing of some products, and there are already parts printed using this technology. The technology has applications in jewelry, footwear, industrial design, architecture, engineering and construction (AEC), automotive, aerospace, dental and medical industries, education, geographic information systems, civil engineering, firearms, and other fields.

# Cutting-edge research on 3D printing 
## 1.	3D printing with AI
The rapid development of 3D printing is inseparable from the continuous improvement of a series of complementary technologies, which complement each other and achieve each other. The convergence of AM technology with artificial intelligence (AI) and robotics means that cutting-edge printing and automation technologies can work together to drive productivity to new heights. With the continuous development of 3D printing technology, it is becoming more and more difficult and cheaper for people to use it. Smaller companies with more agile business models are likely to adopt the technology quickly, challenging industry leaders with innovations. At the same time, cutting-edge companies will increasingly use additive manufacturing to gain a competitive advantage by integrating 3D printing with automation and robotics.
Companies will continue to use new computing and software tools to unlock the limitless potential of additive manufacturing. This is helping to generate new materials and push 4D printing forward - using 3D printing technology to print objects while adding a time dimension or energy source so that their shape or properties change over time.
The medical industry is an early adopter of 3D printing technology, using it to produce prosthetics, implants, and orthopaedic products tailored to individual patients. The medical 3D printing market (including materials, services, software, and hardware) is currently valued at $1.25 billion, and this figure is expected to grow to $6.08 billion by 2027.
![Alt text](../_media/pro03_3d_cutter/cutting_edge1.png)

## 2. 3D printing in the medical industry
"Medical device companies like Stryker are using AM to produce implantable devices, such as artificial knee, hip, and spinal implants, which are typically made of titanium." Kristin Mulherin said, "In order to effectively solve the problem of osseointegration, they developed a proprietary algorithm that allows the metal device to fit into the patient's bone. A 3D printer can create a strong and lightweight implant with a finely processed surface that binds firmly to bone tissue."
Later, 3D printers that can print color functional parts appeared on the market, which also opened up new possibilities and applications for this technology. Over the past few years, surgeons have become accustomed to using 3D technology to create complex anatomical models of organs to help them prepare for surgery. Because additive manufacturing supports color printing, doctors can easily distinguish between veins and arteries. They sometimes print out a 3D model of an individual patient's heart and use it to rehearsed the procedure and find the ideal surgical plan.
![Alt text](../_media/pro03_3d_cutter/cutting_edge2.jpg)



# 3D Printer Test
## Test model Print with two different parameters
### **First Printing**
- **Parameters Setting**
  
    | model/Parameters     | nozzle temperature | platform temperature | fill density | base plate |
    |----------------------|--------------------|----------------------|--------------|------------|
    | model 1              | 205℃              | 30℃                 | 15%         | enabled    |
    | <span style="color:red;">**model 2**             | <span style="color:red;">**220℃**              | <span style="color:red;">**50℃**                 | <span style="color:red;">**30**%         | <span style="color:red;">**Disable**    |

(nozzle temperature 200°; platform temperature30℃；fill density 15%; base plate enabled)

 <figure>
  <img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/para1_1.gif?raw=true" alt="Slicing software import interface" style="width:100%">
  <figcaption style="text-align:center;"> Slicing software import interface</figcaption>
</figure>


 <figure>
  <img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/para1_2.jpg?raw=true" alt="Slice Import Preview" style="width:100%">
  <figcaption style="text-align:center;"> Slice Import Preview</figcaption>
</figure>

<figure>
  <img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/para1_3.jpg?raw=true" alt="Slice  Preview1" style="width:100%">
  <figcaption style="text-align:center;"> Slice Preview 1</figcaption>
</figure>

<figure>
  <img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/para1_4.jpg?raw=true" alt="Slice  Preview2" style="width:100%">
  <figcaption style="text-align:center;"> Slice Preview 2</figcaption>
</figure>

- **Printing process**
 ![Alt text](../_media/pro03_3d_cutter/print1_1.gif)


### Second printing
- **Parameters**
  

    | model/Parameters     | nozzle temperature | platform temperature | fill density | base plate |
    |----------------------|--------------------|----------------------|--------------|------------|
    | **<span style="color:red;">model 1</span>**              | **<span style="color:red;">200℃</span>**              | **<span style="color:red;">30℃</span>**                 | **<span style="color:red;">15%</span>**         | **<span style="color:red;">enabled</span>**    |
    | model 2              | 220℃              | 50℃                 | 30%         | Disable    |


<figure>
  <img src="../_media/pro03_3d_cutter/para2_1.jpg" alt="See the Slice Import Preview gif above for a detailed view of the interface" style="width:100%">
  <figcaption style="text-align:center;"> See the Slice Import Preview gif above for a detailed view of the interface</figcaption>
</figure>

- **Printing process**
 ![Alt text](../_media/pro03_3d_cutter/print2_1.gif)
  ![Alt text](../_media/pro03_3d_cutter/print2_2.gif)
### Comparison of results between two printouts

1.	Parameters Comparison

| model/Parameters     | nozzle temperature | platform temperature | fill density | base plate |
|----------------------|--------------------|----------------------|--------------|------------|
| model 1              | 205℃              | 30℃                 | 15%         | enabled    |
| model 2             | 220℃              | 50℃                 | 30%         | Disable    |

2. 3D Printing result Comparison
    ①nozzle/ platform temperature comparison
    <table align="center"><tr>
    <td><img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/3dresult1.jpg?raw=true" width="300" height="200" border=0></td>
    <td><img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/3dresult2.jpg?raw=true" width="300" height="200" border=0></td>
    </tr></table>
    ②fill density comparison
    <table align="center"><tr>
    <td><img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/3dresult3.png?raw=true" width="300" height="280" border=0></td>
    <td><img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/3dresult4.png?raw=true" width="350" height="280" border=0></td>
    </tr></table>
    ③base plate comparison
    <table align="center"><tr>
    <td><img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/3dresult5.png?raw=true" width="300" height="200" border=0></td>
    <td><img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/3dresult6.jpg?raw=true" width="300" height="200" border=0></td>
    </tr></table>
**Result:** Better quality on the second print

### Test model printing and assemble it
1.	The process of printing.  
![Alt text](../_media/pro03_3d_cutter/test_fusion_model.png)

2.	Remove the supporting structure of the printed model.  
![Alt text](../_media/pro03_3d_cutter/STEP02.gif)

3.	Assemble the parts.  
![Alt text](../_media/pro03_3d_cutter/STEP04.gif)


5.	The result of the 3D print model.  
![Alt text](../_media/pro03_3d_cutter/3dprint_result.png)


# Laser Cutting
## Advantages of laser cutting
### 1.	Material range
All materials common in industrial processing – from steel to aluminum, stainless steel, and non-ferrous metal sheets, all the way to non-metal materials such as plastics, glass, wood, or ceramics – can be cut safely and in high quality with the laser. Very different sheet thicknesses of 0.5 to over 30 millimeters can be cut using the tool. This extremely wide material range makes the laser the top cutting tool for many applications in the area of metals and non-metals.
![Alt text](../_media/pro03_3d_cutter/laser_cutting1.png)

### 2.	Contour freedom
The bundled laser beam only heats up the material locally, and the rest of the workpiece is subjected to minimal thermal stresses or not at all. This means the kerf is barely wider than the beam and even complex, intricate contours may be cut smoothly and free of burrs. Time-consuming post-processing is no longer necessary in most cases. Due to its flexibility, this cutting procedure is often used for small lot sizes, large variant ranges, and in prototype construction.
 <figure>
  <img src="../_media/pro03_3d_cutter/laser_cutting2.png" alt="Slicing software import interface" style="width:100%">
  <figcaption style="text-align:center;">Discover the variety of different cutting procedures</figcaption>
</figure>

## Cutting-edge research on laser cutting
### 1. Flame cutting
In flame cutting, oxygen is used as the cutting gas. The oxygen is blown into the kerf at pressures of up to 6 bar. There, the heated metal reacts with the oxygen: it begins to burn and oxidizes. The chemical reaction releases large amounts of energy - up to five times the laser energy - and assists the laser beam. Flame cutting makes it possible to cut at high speeds and handle jobs involving thick plates such as mild steel with thicknesses in excess of 30 millimeters.
![Alt text](../_media/pro03_3d_cutter/cutting_edge3.png)

### 2. Fusion cutting
Nitrogen or argon is used as the cutting gas here. The gas is blown through the kerf at pressures ranging from 2 to 20 bar. Argon and nitrogen are inert gases.
This means that they do not react with the molten metal in the kerf. They simply blow it out toward the bottom. Simultaneously, they shield the cut edge from the air.
The great advantage of fusion cutting: cut edges are oxide free and do not require further treatment. Nevertheless, the laser beam must supply all of the energy needed for cutting. For this reason, cutting speeds as high as those in flame cutting can be achieved only in thin sheets.
Piercing is also more difficult. Some cutting systems allow you to use oxygen to pierce the material and then switch over to nitrogen for cutting.
![Alt text](../_media/pro03_3d_cutter/cutting_edge4.png)

### 3. Sublimation cutting
This process is rarely used in sheet metal fabrication. Its use, however, becomes attractive in applications involving particularly delicate cutting work. Such applications include the production of stents.
In metal processing, sublimation cutting is the exception;
with nonmetals, it is very common. Many non-metal materials are regularly processed with sublimation cutting. Typical materials include:
• Plastic sheeting and textiles, which vaporize even when only a small amount of energy is applied
• Materials that do not melt, such as wood,
cardboard, or foam
![Alt text](../_media/pro03_3d_cutter/cutting_edge5.png)

</figure>

## Power and Speed Test
1.	The software sets the power and speed of the test pattern hierarchically.
 ![Alt text](../_media/pro03_3d_cutter/cut_square.png)
2.	Cutting test with machine.
 ![Alt text](../_media/pro03_3d_cutter/cutting_test.png)
3.	Two results of the laser cutting.
![Alt text](../_media/pro03_3d_cutter/cut_result.png)
 4.	Statistics on cutting test results.


| Speed/Power | 10 | 20 | 30 | 40 | 50 | 60 | 70 |
|----------|----|----|----|----|----|----|----|
| 10       | ×  | <span style="color: red">√ | √  | √  | √  | √  | √  |
| 20       | ×  | ×  | <span style="color: red">√  | √  | √  | √  | √  |
| 30       | ×  | ×  | <span style="color: red">√  | √  | √  | √  | √  |
| 40       | ×  | ×  | ×  | <span style="color: red">√  | √  | √  | √  |
| 50       | ×  | ×  | ×  | ×  | ×  | <span style="color: red">√  | √  |




## Cutting Accuracy Test
1.	Import cutting target image to the machine.
 ![Alt text](../_media/pro03_3d_cutter/cut_target.png)
2.	Collect the finished materials from the cutter.
 ![Alt text](../_media/pro03_3d_cutter/cut_result2.png)
3.	Measure the actual length to see the error. The width of a single part is 5mm, the number is 10, the total statistical length is 46.75mm, and the error is 3.25mm. Therefore, the value of Kurf is 3.25/10=0.325mm.
 ![Alt text](../_media/pro03_3d_cutter/cut_result3.png)

## Laser Cutting Practice
### 0. Preparation
![Alt text](../_media/pro03_3d_cutter/image-4.png)
<figure>
  <img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/image-4.png?raw=true" alt="Preparation step1" style="width:100%">
  <figcaption style="text-align:center;"> Turn on the master switch</figcaption>
</figure>
<figure>
  <img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/pre_laser1.jpg?raw=true" alt="Preparation step1" style="width:100%">
  <figcaption style="text-align:center;"> Turn on the master switch</figcaption>
</figure>
<figure>
  <img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/pre_laser2.jpg?raw=true" alt="Preparation step2" style="width:100%">
  <figcaption style="text-align:center;"> Turn on the laser</figcaption>
</figure>
<figure>
  <img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/pre_laser3.jpg?raw=true" alt="Preparation step3" style="width:100%">
  <figcaption style="text-align:center;"> Access computer</figcaption>
</figure>


<figure>
  <img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/laser_cad6.jpg?raw=true" alt="Preparation step4" style="width:100%">
   <img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/laser_cad7.jpg?raw=true" alt="Preparation step4" style="width:100%">
    <img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/laser_cad8.jpg?raw=true" alt="Preparation step4" style="width:100%">
    <img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/laser_cad9.jpg?raw=true" alt="Preparation step4" style="width:100%">
    <img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/laser_cad10.jpg?raw=true" alt="Preparation step4" style="width:100%">
  <figcaption style="text-align:center;"> Transport Data</figcaption>
</figure>

<figure>
  <img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/pre_laser4.jpg?raw=true" alt="Preparation step4" style="width:100%">
  <figcaption style="text-align:center;"> Open the lid</figcaption>
</figure>
<figure>
  <img src="../_media/pro03_3d_cutter/laser_cad3.jpg" alt="Preparation step5" style="width:100%">
  <figcaption style="text-align:center;">Moving Laser Position</figcaption>
</figure>
<figure>
  <img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/pre_laser6.jpg?raw=true" alt="Preparation step6" style="width:100%">
  <figcaption style="text-align:center;"> Mobile platforms for positioning 1</figcaption>
</figure>
<figure>
  <img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/pre_laser7.jpg?raw=true" alt="Preparation step7" style="width:100%">
  <figcaption style="text-align:center;"> Mobile platforms for positioning 2</figcaption>
</figure>

### 1.	Draw the shape with Adobe Illustrator.
 ![Alt text](../_media/pro03_3d_cutter/ai.png)

 ### 2.	Import the file into Laser CAD V8.12
![Alt text](../_media/pro03_3d_cutter/laser_cad.png)

### 3.	Set different parameters (power/speed) with different colors in Laser CAD V8.12
![Alt text](../_media/pro03_3d_cutter/laser_cad2.png)

### 4.	Open the Laser cutting machine to location and border running
![Alt text](../_media/pro03_3d_cutter/laser_cad3.jpg)

### 5.	Begin Laser Cutting
![Alt text](../_media/pro03_3d_cutter/laser_cad4.gif)

### 6.	The result of laser cutting
![Alt text](../_media/pro03_3d_cutter/laser_cad5.jpg)