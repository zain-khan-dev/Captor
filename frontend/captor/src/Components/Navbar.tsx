import { Link } from "react-router-dom"


const Navbar = () => {
    return (
        <div className="flex flex-row space-x-4 mx-auto text-xl underline">
            <Link to="/home" ><div className="p-2 cursor-pointer">Home</div></Link>
            <Link to="/audio"><div className="p-2 cursor-pointer">Audio Recog</div></Link>
            <Link to="/video"><div className="p-2 cursor-pointer">Video Recog</div></Link>
            <Link to="/about"><div className="p-2 cursor-pointer">About</div></Link>
        </div>
    )
}

export default Navbar