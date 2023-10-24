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
 ![Alt text](../_media/pro03_3d_cutter/para1_1.png)
 ![Alt text](../_media/pro03_3d_cutter/para1_2.png)
 ![Alt text](../_media/pro03_3d_cutter/para1_3.png)
- **Printing process**
 ![Alt text](../_media/pro03_3d_cutter/print1_1.png)
![Alt text](../_media/pro03_3d_cutter/print1_2.png)

### Second printing
- **Parameters**
 ![Alt text](../_media/pro03_3d_cutter/para2_1.png)
 ![Alt text](../_media/pro03_3d_cutter/para2_2.png)
 ![Alt text](../_media/pro03_3d_cutter/para2_3.png)
- **Printing process**
 ![Alt text](../_media/pro03_3d_cutter/print2_1.png)
 ![Alt text](../_media/pro03_3d_cutter/print2_2.png)
### Comparison of results between two printouts
1. **First Time** (nozzle temperature 210°; fill density 15%; base plate enabled) 
   ![Alt text](../_media/pro03_3d_cutter/3dresult1.png)
2. **Second Time**(nozzle temperature 200°; filling density 20%; base plate not activated) 
   ![Alt text](../_media/pro03_3d_cutter/3dresult2.png)
**Result:** Better quality on the second print

### Test model printing and assemble it
1.	The process of printing.  
![Alt text](../_media/pro03_3d_cutter/test_fusion_model.png)

2.	Remove the supporting structure of the printed model.  
![Alt text](../_media/pro03_3d_cutter/STEP02.gif)

3.	Polish the model for better quality of the surface.  
![Alt text](../_media/pro03_3d_cutter/STEP03.gif)

4.	Assemble the parts  
![Alt text](../_media/pro03_3d_cutter/STEP05.gif)

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


| Speed/Power | 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 |
|-------------|----|----|----|----|----|----|----|----|----|
| 10          | ×  | <span style="background-color: yellow">√</span>   | √  | √  | √  | √  | √  | √  | √  |
| 20          | ×  | ×  | <span style="background-color: yellow">√</span>  | √  | √  | √  | √  | √  | √  |
| 30          | ×  | ×  | <span style="background-color: yellow">√</span>  | √  | √  | √  | √  | √  | √  |
| 40          | ×  | ×  | ×  | ×  |<span style="background-color: yellow">√</span>   | √  | √  | √  | √  |
| 50          | ×  | ×  | ×  | ×  | ×  | <span style="background-color: yellow">√</span>  | √  | √  | √  |



## Cutting Accuracy Test
1.	Import cutting target image to the machine.
 ![Alt text](../_media/pro03_3d_cutter/cut_target.png)
2.	Collect the finished materials from the cutter.
 ![Alt text](../_media/pro03_3d_cutter/cut_result2.png)
3.	Measure the actual length to see the error. The width of a single part is 5mm, the number is 10, the total statistical length is 46.75mm, and the error is 3.25mm. Therefore, the value of Kurf is 3.25/10=0.325mm.
 ![Alt text](../_media/pro03_3d_cutter/cut_result3.png)

