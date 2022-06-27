import {FormEvent, LegacyRef, useState} from "react"
import React from "react"

const AudioRecog = () => {
    const fileRef:React.RefObject<HTMLInputElement> = React.createRef()

    const handleSubmit = (e:FormEvent<HTMLFormElement>) => {
        e.preventDefault()
        console.log("send file")
        if(fileRef.current != null && fileRef.current.files != null)
            console.log(fileRef.current.files[0])
    }
    


    return (
        <div>
            <div>Audio Recognition here</div>
            <div>Please select a file to recognize</div>
            <form onSubmit={handleSubmit}>
                <input type="file" ref={fileRef} />
                <button type="submit"  > Submit</button>
            </form>
        </div>
    )
}

export default AudioRecog