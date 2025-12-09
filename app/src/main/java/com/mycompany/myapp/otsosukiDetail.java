package com.mycompany.myapp;

import android.database.*;
import android.database.sqlite.*;
import android.os.*;
import android.support.annotation.*;
import android.support.v7.app.*;
import android.view.*;
import android.widget.*;
import android.content.*;

public class otsosukiDetail extends AppCompatActivity {
int id;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    setContentView(R.layout.otsosuki_detail);
    action();

    }
    public void action(){
        int id=(int) getIntent().getExtras().get(Otsosuki.ID);

		this.id=id;
		
		SQLiteOpenHelper helper=new SQL(this);
		
		try{	
			SQLiteDatabase db=helper.getReadableDatabase();
			//read the date we want to
//			Cursor cursor=db.query("SHINOBI",new String[]{"_id","Name","Description"},null,null,null,null,null);
//or we can order Name table in ascending order

			//	Cursor cursor2=db.query("SHINOBI",new String[]{"_id","Name","Description"},null,null,null,null,null,"Name ASC");

			// in the same way we will be able to order in descending way

			//	Cursor cursor3=db.query("SHINOBI",new String[]{"_id","Name","Description"},null,null,null,null,null,"Name DESC");

			//or we return our selected records
			//in this case we just want to return Hagoromo row

			//Name=? means to return all records which contains Latte word in Name collumn

			//	Cursor cursor4=db.query("SHINOBI",new String[]{"_id","Name","Description"},"Name=?",

			//	new String[]{"Hogoromo"},null,null,null);

			//or

			//it must be String array even though we want to pass another type of variables
			//here is how to convert int to String

			Cursor cursor5=db.query("SHINOBI",new String[]{"NAME","DESCRIPTION","IMAGE_RESOURCE","FAVORITE"},"_id=?",
			new String[]{Integer.toString(id)},null,null,null);
if(cursor5.moveToFirst()){
	
String text1=cursor5.getString(0);
	
String text2=cursor5.getString(1);
int img=cursor5.getInt(2);
boolean isFavorite=(cursor5.getInt(3)==1);

CheckBox favorite=(CheckBox)findViewById(R.id.favorite);
favorite.setChecked(isFavorite);

TextView title_text=(TextView)findViewById(R.id.title);
title_text.setText(text1);

TextView description=(TextView)findViewById(R.id.discription);
description.setText(text2);

ImageView image=(ImageView)findViewById(R.id.action_image);
image.setImageResource(img);


	
}
cursor5.close();
db.close();
		}catch(Exception ex){
			Toast toast=Toast.makeText(this,"Database is unavaliable",Toast.LENGTH_SHORT);

			toast.show();
		
			}

		
		toolbar();

		 
		}
	
private void toolbar(){

    ActionBar upbutton=getSupportActionBar();
    upbutton.setDisplayHomeAsUpEnabled(true);
}

public void onFavoriteClicked(View v){


	
SQLiteOpenHelper helper=new SQL(this);
	CheckBox checkbox=(CheckBox)findViewById(R.id.favorite);
	
	ContentValues content=new ContentValues();
	
	content.put("FAVORITE",checkbox.isChecked());
	
try{
SQLiteDatabase db=helper.getReadableDatabase();

db.update("SHINOBI",content,"_id",new String[]{Integer.toString(this.id)});

}

 
catch(SQLException ex){
	Toast toast=Toast.makeText(this,"Database is unavaliable",Toast.LENGTH_SHORT);
toast.show();
	}	
	
	}
	
int getId(){
	return id;
}
}
