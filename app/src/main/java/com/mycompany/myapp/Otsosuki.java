package com.mycompany.myapp;

import android.content.*;
import android.database.*;
import android.database.sqlite.*;
import android.os.*;
import android.support.annotation.*;
import android.support.v7.app.*;
import android.view.*;
import android.widget.*;



public class Otsosuki extends AppCompatActivity{
	SQLiteDatabase db;
	Cursor cursor;
	 
    public  static final String ID="idforintent";
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    setContentView(R.layout.otsosuki_list);
        toolbar();
		ListView listView = (ListView) findViewById(R.id.list2);
		
		
		
		 
		SQLiteOpenHelper helper=new SQL(this);
		try{
			db=helper.getReadableDatabase();
			cursor=db.query("SHINOBI",new String[]{"_id","NAME"},null,null,null,null,null);
			SimpleCursorAdapter sca=new SimpleCursorAdapter(this,
															android.R.layout.simple_list_item_1,cursor,new String[]{"NAME"},new int[]{android.R.id.text1},0);
			
listView.setAdapter(sca);
			
		}
		catch(SQLiteException ex){
			Toast toast=Toast.makeText(this,"Database is unvaliable",Toast.LENGTH_SHORT);
			toast.show();
		}
   
   


            AdapterView.OnItemClickListener itemClickListener=new AdapterView.OnItemClickListener() {
                @Override
                public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                    Intent intent = new Intent(Otsosuki.this, otsosukiDetail.class);
                    intent.putExtra(ID, (int) id);
                    startActivity(intent);
                }


            };

        listView.setOnItemClickListener(itemClickListener);

            }

public void toolbar(){

            ActionBar actionBar=getSupportActionBar();
            actionBar.setDisplayHomeAsUpEnabled(true);

			}




@Override
protected void onDestroy()
{
	// TODO: Implement this method
	super.onDestroy();
db.close();
cursor.close();
	
	}



}


