import MDEditor from "@uiw/react-md-editor";
import { useState } from "react";

interface EditorProps {
  onSave: (content: string) => void;
}

export default function Editor({ onSave }: EditorProps) {
  const [value, setValue] = useState<string>("");

  return (
    <div>
      <MDEditor value={value} onChange={(val) => setValue(val || "")} />
      <button onClick={() => onSave(value)}>Save to Google Drive</button>
    </div>
  );
}