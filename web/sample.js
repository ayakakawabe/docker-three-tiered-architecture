const appUrl="http://app:8000";

const fetchApp=async()=>{
    const response= await fetch(appUrl);
    const data=response.json();
    return data;
};

(async()=>{
    try{
        const data= await fetchApp();
        console.log(data);
    }catch(error){
        console.log(error);
    };
})();