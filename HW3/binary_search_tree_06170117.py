#!/usr/bin/env python
# coding: utf-8

# In[157]:


class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    
    def insert(self, root, val): 
        if root.val == None:
            root.val = val     
        
        else:
            if val <= root.val :
                if root.left == None: 
                    root.left=val
                else:
                    self.insert(root.left,val)   
                
            elif val > root.val:
                if root.right == None:
                        root.right=val
                else:
                    self.insert(root.right,val)
        return val
      
                
    def search(self,root,target): 
    
        if root.val == target:
            root.val=target
            return root
        
        elif root != target:
            if target <= root.val:
                if root.left==None:
                    return None
                else:
                    return self.search(root.left,target)
                    
            elif target > root.val:
                if root.right==None:
                    return None
                else:
                    return self.search(root.right,target)
                
                
    def delete(self, root, target):
        def getMax(root):       
            while root.right:
                root=root.right
            return root
        if root == None:
            return root
        
        elif target < root.val:
            root.left = self.delete(root.left,target)
            
        elif target > root.val:
            root.right = self.delete(root.right,target)
        else:
            if root.left is None:  
                a = root.right
                root = None
                return a
            elif root.right is None: 
                a = root.left
                root = None
                return a
            elif root.right and root.left:
                a = getMax(root.left) 
                root.val = a.val   
                root.left = self.delete(root.left, temp.val)  
        return root
        
        
                
   
          
    def modify(self, root, target, new_val):   
        root=self.delete(root,target)  
        print("delete ok")            
        self.insert(root,new_val)  
        print("insert ok")
        return root
        
   

