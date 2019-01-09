INSERT INTO `student_academic_details` VALUES ('302','1700AA00302','HSC / 12th (Sci); or Equivalent','B.C.G. Public H.S. School Dewas','Madhya Pradesh Board of Secondary Education, Bhopal',2016,'Science','FIRST','50.0','ENGLISH','',34,100,52,100,'Chemistry',58,100,'',NULL,NULL,NULL,NULL);
INSERT INTO `student_academic_details` VALUES ('303','1700AA00303','HSC / 12th (Sci); or Equivalent','B.C.G. Public H.S. School Dewas','Madhya Pradesh Board of Secondary Education, Bhopal',2016,'Science','FIRST','50.96938775510204','ENGLISH','',34,100,52,100,'Chemistry',58,100,'',NULL,NULL,NULL,NULL);
INSERT INTO `student_master` VALUES (1,216,'1700AA00302',1,1001,5,5,1,23,'testName','  ','ABC','1997-09-30','1A/G1 JAI SHREE VILLA','SANCHAR NAGAR MAIN KANADIA ROAD','',323,9,1,'452016','','','','1234567890','1A/G1 JAI SHREE VILLA','SANCHAR NAGAR MAIN INDORE','',323,9,1,'123456',113,3,'',NULL,0,'A',1,0,NULL,100,70,NULL,'abc@student.suas.ac.i','1234','1234',42,'2018-05-31',0,'2017-02-11 00:00:00',NULL,'','',NULL);
INSERT INTO `srm_gradecard_issued` VALUES ('302','1700AA00302',1111,1,120,1,'pass','8.0',NULL,'2018-02-17','2018-01-17');
INSERT INTO `student_master` VALUES (1,216,'1700AA00303',1,1001,5,5,1,23,'testName','  ','ABC','1997-09-30','1A/G1 JAI SHREE VILLA','SANCHAR NAGAR MAIN KANADIA ROAD','',323,9,1,'452016','','','','1234567890','1A/G1 JAI SHREE VILLA','SANCHAR NAGAR MAIN INDORE','',323,9,1,'123456',113,3,'',NULL,0,'A',1,0,NULL,100,70,NULL,'abc@student.suas.ac.i','1234','1234',42,'2018-05-31',0,'2017-02-11 00:00:00',NULL,'','',NULL);
INSERT INTO `srm_gradecard_issued` VALUES ('303','1700AA00303',1111,1,120,1,'pass','7.8',NULL,'2018-02-17','2018-01-17');

delete from student_academic_details where student_id="1700AA00302";
delete from student_master where student_id="1700AA00302";
delete from srm_gradecard_issued where studentid="1700AA00302";
