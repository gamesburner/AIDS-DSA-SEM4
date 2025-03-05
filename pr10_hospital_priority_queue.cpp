#include <iostream>
#include<string>
using namespace std;

string Q[10];
int pr[10];
int r=-1,f=-1,n;

void enqueue(string data, int p){
    int i;
    if((f==0)&&(r==n-1))
    cout<<"Queue is full";
    else{
        if(f==-1){
            f=r=0;
            Q[r]=data;
            pr[r]=p;
            }
            else {
                for(i=r;i>=f;i--){
                    if(p>pr[i]){
                        Q[i+1]=Q[i];
                        pr[i+1]=pr[i];
                    }
                    else break;
                }
            
            Q[i+1]=data;
            pr[i+1]=p;
            r++;
    }
}
}

void dequeue(){
    if(f==-1){
        cout<<"Queue is Empty";
    }
    else{
        cout<<"Element deleted = "<<Q[f]<<endl;
        cout<<"Element Priority = "<<pr[f]<<endl;
        if(f==r) f=r=-1;
        else f++;
    }
}

void print(){
    int i;
    for(i=f;i<=r;i++){
        cout<<"\nPatient Name: "<<Q[i];
        switch(pr[i]){
            case 1: cout<<" Priority: ketchup";
            break;
            case 2: cout<<" Priority: non-serious";
            break;
            case 3: cout<<" Priority: highly-serious";
            break;
            default:
            cout<<" Priority Not Found";
        }
    }

}

int main(){
    string data;
    int opt,i,p;
    

    do{
        cout<<"\n\n1. insert data in queue\n2. show data of the queue\n3. delete data from the queue\n4. Exit\n";
        cout<<"Enter your choice : ";
        cin>>opt;
        switch (opt)
        {
        case 1:
            cout<<"enter no of patients"<<endl;
            cin>>n;
            for(i=0;i<n;i++){
                cout<<"Enter Patient Name: ";
                cin>>data;
                cout<<"Enter Priority: ";
                cin>>p;
                enqueue(data,p);
            }
            break;
        
        case 2:
            print();
            break;

        case 3:
            dequeue();
            break;  
        }
    }while (opt!=4);
    return 0;
    }
    