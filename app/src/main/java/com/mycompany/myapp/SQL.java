     package com.mycompany.myapp;
import android.content.*;
import android.database.sqlite.*;

public class SQL extends SQLiteOpenHelper
{
	
	public static final String name="gg ";
	public static final int VERSION=2;
public SQL(Context context){
	super(context,name,null,VERSION);
}
	@Override
	public void onCreate(SQLiteDatabase db)
	{
		// TODO: Implement this method
		updatemydatabase(db,0,VERSION);

		}

	@Override
	public void onUpgrade(SQLiteDatabase p1, int p2, int p3)
	{
		// TODO: Implement this method
	
	updatemydatabase(p1,p2,p3);
	}
	
	private static void insert(SQLiteDatabase db,String name,String description,int img){
	ContentValues content=new ContentValues();
	content.put("NAME",name);
	content.put("DESCRIPTION",description);
	content.put("IMAGE_RESOURCE",img);
	db.insert("SHINOBI",null,content);
	}
private void updatemydatabase(SQLiteDatabase db,int old,int newv ){
	if(old<1){
	db.execSQL("CREATE TABLE SHINOBI ("+"_id INTEGER PRIMARY KEY AUTOINCREMENT,"+"NAME TEXT,"+"DESCRIPTION TEXT,"
			   +"IMAGE_RESOURCE INTEGER);");

		insert(db,"Kaguya","the best of Kaguya ",R.drawable.kaguya);
		insert(db,"Hagoromo","the best of Hagoromo",R.drawable.hagoromo);
	insert(db,"Hamura","the best of moon",R.drawable.hamura);
	
	}
	
	if(old<2){
	//if this our old version is lower than it will add new column "Favourite"	
		db.execSQL("ALTER TABLE SHINOBI ADD COLUMN FAVORITE NUMERIC;");	
	
		}
	}




	
	}		
