#!/bin/sh
# by zhangxuchen01

file=$1
label_index=2
q_index=1
line_number=`wc -l $file | awk '{print $1}'`
cat $file | sort -k $q_index -n | awk -v label_index="${label_index}" -v q_index="${q_index}" -v line_number="${line_number}" '{
             label[NR]=$label_index;
             rank[NR]=line_number-NR+1
             if (label[NR]=="0"){
                 M=M+1
             }else{
                 N=N+1
             }
             if (NR==1){
                 previous_q=$q_index;
                 start_index=NR;
             }else{
                 if ($q_index!=previous_q){
                     temp1=rank[start_index]
                     temp2=rank[NR-1]
                     temp=(temp1+temp2+0.0)/2
                     for (i=start_index;i<=NR-1;i++){
                         rank[i]=temp;
                     }
                     start_index=NR;
                 }
             }
         }
         END{
             temp1=rank[start_index]
             temp2=rank[line_number]
             temp=(temp1+temp2)/2
             for (i=start_index;i<=line_number;i++){
                 rank[i]=temp;
             }
             ans=0
             for (i=1;i<=line_number;i++){
                 if (label[i]==0){
                     ans=ans+rank[i];
                 }
             }
             ans=(ans+0.0)/M/N-(M+1.0)/2/N
             print ans
         }'
         
