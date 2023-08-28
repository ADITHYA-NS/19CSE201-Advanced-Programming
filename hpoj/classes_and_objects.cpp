#include<iostream>
using namespace std;
class BankAccount{
string accname;
float balance;
public:
    int accnum;
    void setdetails(string an, int ac ,float bal){
        accname=an;
        accnum=ac;
        balance=bal;
        
    }
    BankAccount(){
        cout<<"Bank Account Created Successfully"<<endl;
    }
    void DisplayDetails(){
        cout<<"Account Holder: "<<accname<<endl;
        cout<<"Account Number: "<<accnum<<endl;
        cout<<"Current Balance: ₹"<<balance<<endl;
    }
    void Deposit( float dep){
        balance=balance+dep;
        cout<<"Deposited ₹"<<dep<<" into the account."<<endl;
    }
    void Withdraw(float wd){
        if(balance-wd>0){
            balance=balance-wd;
            cout<<"Withdrawn ₹"<<wd<<" from the account."<<endl;
        }
        else{
            cout<<"Insufficient balance or invalid withdrawal amount."<<endl;
        }
    }
};
int main(){
    BankAccount b;
    string acname;
    int acnum;
    float balance;
    float dep;
    float wd1;
    float wd2;
    cin>>acname;
    cin>>acnum;
    cin>>balance;
    cin>>dep;
    cin>>wd1;
    cin>>wd2;
    b.setdetails(acname,acnum,balance) ;
    b.DisplayDetails();  
    b.Deposit(dep);
    b.Withdraw(wd1);
    b.Withdraw(wd2);
    b.DisplayDetails();  
    return 0;
}
