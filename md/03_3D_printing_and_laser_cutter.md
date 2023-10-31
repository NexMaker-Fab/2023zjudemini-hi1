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
    | model 1              | 200℃              | 30℃                 | 15%         | enabled    |
    | <span style="color:red;">**model 2**             | <span style="color:red;">**220℃**              | <span style="color:red;">**50℃**                 | <span style="color:red;">**30**%         | <span style="color:red;">**Disable**    |

(nozzle temperature 200°; platform temperature30℃；fill density 15%; base plate enabled)

 ![Alt text](../_media/pro03_3d_cutter/para1_1.gif)
 ![Alt text](../_media/pro03_3d_cutter/para1_2.gif)
 ![Alt text](../_media/pro03_3d_cutter/para1_3.gif)
- **Printing process**
 ![Alt text](../_media/pro03_3d_cutter/print1_1.gif)
![Alt text](../_media/pro03_3d_cutter/print1_2.png)

### Second printing
- **Parameters**
  

    | model/Parameters     | nozzle temperature | platform temperature | fill density | base plate |
    |----------------------|--------------------|----------------------|--------------|------------|
    | **<span style="color:red;">model 1</span>**              | **<span style="color:red;">200℃</span>**              | **<span style="color:red;">30℃</span>**                 | **<span style="color:red;">15%</span>**         | **<span style="color:red;">enabled</span>**    |
    | model 2              | 220℃              | 50℃                 | 30%         | Disable    |

 ![Alt text](../_media/pro03_3d_cutter/para2_1.gif)
- **Printing process**
 ![Alt text](../_media/pro03_3d_cutter/print2_1.gif)
  ![Alt text](../_media/pro03_3d_cutter/print2_2.gif)
### Comparison of results between two printouts
1. **First Time** (nozzle temperature 210°; fill density 15%; base plate enabled) 
   ![Alt text](../_media/pro03_3d_cutter/3dresult1.jpg)
2. **Second Time**(nozzle temperature 200°; filling density 20%; base plate not activated) 
   ![Alt text](../_media/pro03_3d_cutter/3dresult2.jpg)
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
| 10       | ×  | <span style="color: red">√</span> | √  | √  | √  | √  | √  |
| 20       | ×  | ×  | <span style="color: red">√</span>  | √  | √  | √  | √  |
| 30       | ×  | ×  | <span style="color: red">√</span>  | √  | √  | √  | √  |
| 40       | ×  | ×  | ×  | <span style="color: red">√</span>  | √  | √  | √  |
| 50       | ×  | ×  | ×  | ×  | ×  | <span style="color: red">√</span>  | √  |




## Cutting Accuracy Test
1.	Import cutting target image to the machine.
 ![Alt text](../_media/pro03_3d_cutter/cut_target.png)
2.	Collect the finished materials from the cutter.
 ![Alt text](../_media/pro03_3d_cutter/cut_result2.png)
3.	Measure the actual length to see the error. The width of a single part is 5mm, the number is 10, the total statistical length is 46.75mm, and the error is 3.25mm. Therefore, the value of Kurf is 3.25/10=0.325mm.
 ![Alt text](../_media/pro03_3d_cutter/cut_result3.png)

## Laser Cutting Practice
### 1.	Draw the shape with Adobe Illustrator.
 ![Alt text](../_media/pro03_3d_cutter/ai.png)

 ### 2.	Import the file into Laser CAD V8.12
![Alt text](../_media/pro03_3d_cutter/laser_cad.png)

### 3.	Set different parameters (power/speed) with different colors in Laser CAD V8.12
![Alt text](../_media/pro03_3d_cutter/laser_cad2.png)

### 4.	Open the Laser cutting machine to location and border running
![Alt text](../_media/pro03_3d_cutter/laser_cad3.png)

### 5.	Begin to laser cutting
![Alt text](../_media/pro03_3d_cutter/laser_cad4.gif)

### 6.	The result of laser cutting
![Alt text](../_media/pro03_3d_cutter/laser_cad5.jpg)