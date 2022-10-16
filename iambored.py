#! /usr/bin/env python3

# TODO pattern을 구현하고 결과를 주석에 달기

import time

sentence = "IamBored!"
length_of_sentence = len(sentence)
WIDTH = 30
TIMES = 30

# for문을 이용할 수 있다.
# while문을 이용할 수 있다.

# format을 이용할 수 있다.
# spaces를 이용할 수 있다.
# TODO patterns를 어떤 식으로 만들 수 있는가?

# pattern1 = 한 칸씩 오른쪽 왼쪽으로 왔다갔다하기
# pattern2 = 글자 하나씩 한 칸으로 이동하여 끝에 뭉치고 다시 반대로 가기
# pattern3 = patten1에서 끝지점에서 한글자 남을 때까지 갔다가 다시 돌아오기

# pattern1
n = 0
for i in range(TIMES):
    for j in range(WIDTH - length_of_sentence):
        spaces = ' ' * j
        if (n // (WIDTH - length_of_sentence)) % 2 == 0:
            print(spaces + sentence)
        else:
            left = ' ' * (WIDTH - (j + length_of_sentence))
            print(left + sentence + spaces)
        time.sleep(0.1)
        n += 1

# pattern2
"""
iambored!
iambored !
iambored  !
iambored   !
iambored    !
iambored     !
iambored      !
iambored       !
iambored        !
iambored         !
iambored          !
iambore d         !
iambore  d        !
iambore   d       !
iambore    d      !
iambore     d     !
iambore      d    !
iambore       d   !
iambore        d  !
iambore         d !
iambore          d!
iambor e         d!
...
i          ambored!
 i         ambored!
  i        ambored!
   i       ambored!
    i      ambored!
     i     ambored!
      i    ambored!
       i   ambored!
        i  ambored!
         i ambored!
          iambored!
         i ambored!
        i  ambored!
       i   ambored!
...
iambored!
"""
for i in range(TIMES):
    ...


# pattern3
"""
iambored!
iambored !
iambore d !
iambor e d !
iambo r e d !
iamb o r e d !
iam b o r e d !
ia m b o r e d !
i a m b o r e d !
 i a m b o r e d !
  i a m b o r e d !
   i a m b o r e d!
    i a m b o r ed!
     i a m b o red!
      i a m b ored!
       i a m bored!
        i a mbored!
         i ambored!
          iambored!
         i ambored!
       i a m bored!
...
iambo r e d !
iambor e d !
iambore d !
iambored !
iambored!
"""

# pattern4

"""
IamBored!
 IamBored!
  IamBored!
   IamBored!
    IamBored!
     IamBored!
      IamBored!
       IamBored!
        IamBored!
         IamBored!
          IamBored!
           IamBored!
            IamBored!
             IamBored!
              IamBored!
               IamBored!
                IamBored!
                 IamBored!
                  IamBored!
                   IamBored!
                    IamBored!
                     IamBored!
                      IamBored
                       IamBore
                        IamBor
                         IamBo
                          IamB
                           Iam
                            Ia
                             I
                            Ia
                           Iam
                          IamB
                         IamBo
                        IamBor
                       IamBore
                      IamBored
                     IamBored!
                    IamBored! 
                   IamBored!  
                  IamBored!   
                 IamBored!    
                IamBored!     
               IamBored!      
              IamBored!       
             IamBored!        
            IamBored!         
           IamBored!          
          IamBored!           
         IamBored!            
        IamBored!             
       IamBored!              
      IamBored!               
     IamBored!                
    IamBored!                 
   IamBored!                  
  IamBored!    
...
"""

# pattern5

"""
Iambored!I
Iambored!Ia
Iambored!Iam
Iambored!IamB
Iambored!IamBo
Iambored!IamBor
Iambored!IamBore
Iambored!IamBored
Iambored!IamBored!
Iambored!IamBored!I
...
IamBored!IamBored!IamBored!IamBored!
IamBored!IamBored!IamBored!IamBored
IamBored!IamBored!IamBored!IamBore
IamBored!IamBored!IamBored!IamBor
IamBored!IamBored!IamBored!IamBo
IamBored!IamBored!IamBored!IamB
...
IamBored!
"""
