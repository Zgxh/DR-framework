function drawfig()

load teapot.mat
teapots=255*X;
d=2;
m=400;
indx=1:400;
teapots=teapots(:,indx(1:2:m));
k = [2,3,4,5];
row=5;
col=7;
ks=1:4:size(teapots,2);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%  降维实验  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
for i=1:row
    
    K=1+i;

    % 1. LLE
    [poses]=lle(teapots,K,d); 
    subplot(row,col,(i-1)*col+1)
    showFacesOnR2(teapots,poses,ks);

    % % %  % 2. HLLE 未使用，跑不动
    % % %   [poses] = hlle(teapots', d, K, 'eig_impl');
    % % %  subplot(row,col,(i-1)*col+2)
    % % %  showFacesOnR2(teapots,poses,ks);

    %  3. LLC
    [poses] = run_llc(teapots, d, K, 1, 200,'eig_impl');
    subplot(row,col,(i-1)*col+2)
    showFacesOnR2(teapots,poses,ks);

    % 4. LTSA
    [poses,err] = ltsa(teapots, d, K);
    subplot(row,col,(i-1)*col+3)
    showFacesOnR2(teapots,poses,ks);

%     %  5. MLLE
%     [poses,err] = Mlle(teapots, d, K);
%     subplot(row,col,(i-1)*col+4)
%     showFacesOnR2(teapots,poses,ks);

    % 6. IHNE
    [poses] = IHNE(teapots,K,d);
    subplot(row,col,(i-1)*col+5)
    showFacesOnR2(teapots,poses,ks);

    % 7. RHNE
    [poses, ~] = RHNE(teapots,K,d);
    subplot(row,col,(i-1)*col+6)
    showFacesOnR2(teapots,poses,ks);

    % 8. BHNE
    [poses, ~] = BHNE(teapots,K,d);
    subplot(row,col,(i-1)*col+7)
    showFacesOnR2(teapots,poses,ks);

end