package com.mycompany.myapp;

import android.provider.ContactsContract;

public class Database {


private int img;
private  String name;
private String discription;
    public static Database[]databases={new Database(R.drawable.kaguya,"Kaguya",
            "For the episode, head to Kaguya Ōtsutsuki. 大筒木カグヤ Ōtsutsuki Kaguya. ... Princess Kaguya Ōtsutsuki (大筒木カグヤ, Ōtsutsuki Kaguya) is the former matriarch of the Ōtsutsuki clan and mother of Hagoromo and Hamura Ōtsutsuki."
            )
            ,new Database(R.drawable.hagoromo,"Hagoromo","Hagoromo Ōtsutsuki (大筒木ハゴロモ, Ōtsutsuki Hagoromo), known to Earth's population at large as the Sage of Six Paths (六道仙人, Rikudō Sennin"),
            new Database(R.drawable.hamura,"Hamura","Hamura Ōtsutsuki (大筒木ハムラ, Ōtsutsuki Hamura) was the son of Princess Kaguya Ōtsutsuki , the fraternal twin brother of Hagoromo Ōtsutsuki")};
    public Database(int img,String name,String discription){
        this.img=img;
        this.name=name;

        this.discription=discription;
    }

    public String getName(){
        return name;
    }

    public int getImg() {
        return img;
    }

    public String getdiscription(){

        return discription;
    }

    @Override
    public String toString() {
        return name;
    }

	
	}
