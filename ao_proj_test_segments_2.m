clearvars; clc; close all;
files = [{'nuty.jpg'}, {'nuty2.jpg'}];
cols = 2;
poz = 1;
licznik=0;

for k=1:length(files)
    im = double(rgb2gray(imread(files{k}))/255);
    %figure
    %imshow(im)
    bin = imbinarize(im);

    bin = imclose(bin, ones(2));
    bin = imopen(bin, ones(8));
    bin = imdilate(bin, ones(3));
    bin=~bin;

    l = bwlabel(bin);
    
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    fun = {@AO5RShape, @AO5RCircularityL, @AO5RCircularityS, @AO5RMalinowska, @AO5RHaralick, @AO5RDanielsson}; % tablica "wskaznikow" do funkcji
    a=regionprops(bin, 'all');
    cir = zeros(length(a), length(fun));
    
    for i=1:length(a)
        tmp=a(i).Image;
        for j=1:length(fun)
            cir(i,j) = fun{j}(tmp);
        end
    end
    %%%%%%%%%

    m = mean(cir);
    s = std(cir);

    odch = abs((cir-m)./s);
    
   
    for i=1:length(odch)
        if odch(i, :)>0.25
            l(l==i) = 0;
        end
    end

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    

    binSegmentation = imdilate(l>0, ones(15));
    binSegmentation([1, end], :) = 1;
    binSegmentation(:, [1, end]) = 1;
    d = bwdist(binSegmentation, 'cityblock');
    lSegmentation = watershed(d);
    figure
    imshow(label2rgb(lSegmentation));
    
    figure;
   
    % for i=1:length(lSegmentation)
    %    imshow(lSegmentation == i .* im); 
    %end
    
    arrayDataWithDividedSemgents = lSegmentation;
    save segemntsForLearning.mat arrayDataWithDividedSemgents;
    
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    licznik = licznik + 1;
    save(strcat('cir', string(licznik)), 'odch')

    tmp = label2rgb(l);
    tmp = 255-tmp;
    figure;
    imshow(uint8(im*255)+tmp);

    figure
    imshow(lSegmentation>0 & imbinarize(im))
    
end

