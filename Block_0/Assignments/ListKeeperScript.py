class ListKeeper(object):  

    named_list=dict()

    def __init__(self):
        super().__init__()        
        self.named_list['example']=[1,2,3,4,5]
                 
    def show(self):
        """Returns all list names

        Returns:
            list: List with all names
        """        
        return list(self.named_list.keys())
             
    def add(self, name, list):
        """Adds a new list

        Args:
            name (string): Name of the list
            list (list): Added list
        """        
        self.named_list[name]=list
        
    
    def delete(self,name):     
        """Deletes specific list

        Args:
            name (string): Name of the list
        """           
        del self.named_list[name]        
    
    def sort(self, name):
        """Returns the sorted list name

        Args:
            name (string): Name of the list

        Returns:
            list: Sorted list
        """        
        return sorted(self.named_list[name])

    def append(self,name,list):
        """Appends given list to the list with the name

        Args:
            name (string): Name of the list
            list (list): Appended list
        """        
        self.named_list[name]=self.named_list[name]+list
    
    def get(self,name):
        """Get the list with the name

        Args:
            name (string): Name of the list

        Returns:
            list: List with the specific name
        """        
        return self.named_list[name]

