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
  <img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/pre_laser4.jpg?raw=true" alt="Preparation step4" style="width:100%">
  <figcaption style="text-align:center;"> Open the lid</figcaption>
</figure>
<figure>
  <img src="https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_media/pro03_3d_cutter/pre_laser5.jpg?raw=true" alt="Preparation step5" style="width:100%">
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