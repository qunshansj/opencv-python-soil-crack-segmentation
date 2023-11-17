
I=imread('lena.bmp');
I=im2double(I);
%figure;
%imshow(I);title('org img');
 
[height width R]=size(I);
for i=2:height-1
    for j=2:width-1
       L(i,j)=4*I(i,j)-I(i-1,j)-I(i+1,j)-I(i,j-1)-I(i,j+1);
    
    end
end
%figure;
%imshow(L,[]);
 
%G(i,j)=0.3*L(i,j)+0.7*I(i,j);
%figure;
%imshow(G,[]);
 
for i=1:height-1
    for j=1:width-1
        if (L(i,j)<0.2)
            L(i,j)=1;
        else L(i,j)=0;
        end
    end
end
figure;
imshow(L,[]);
 